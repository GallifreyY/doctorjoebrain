from util import *
import json
import re

components = {
    "usbdisk": "ClientDriveRedirection",
    "printers": ["ThinPrint","PrintRedir"],
    "scanners": "ScannerRedirection",
    "cameras": "RTAV"
}

docGUIDlinks = {
    "CDR": "GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html",
    "usbdisk": "GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html",
    "printers": "GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html",
    "scanners": "GUID-303F68FD-0CC1-4C9E-81ED-10C274669B93.html",
    "cameras": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html",
    "RTAV": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html"
}


def diagnosis(collected_data, device):
    suggestion = []
    error = []
    warning = []
    collected_data = collected_data

    # todo: general
    if device.problemcode!=None:
        if int(device.problemcode) > 0:
            ss="This device has some configuration issues. The device problem code is {}. {}".format(device.problemcode, device.problemdesc)
            sslink = "https://support.microsoft.com/en-us/help/310123/error-codes-in-device-manager-in-windows"
            error.append([ss,sslink])
    if device.is_present == False:
            error.append("Please make sure this device is connected to your client machine by USB physically.")
    if device.is_reboot_needed == True:
            warning.append("Please reboot your client machine OS to make this device work properly.")

    # todo: detect components in Horizon
    comp = components.get(device.type, None)
    if comp is not None:
        if isinstance(comp,list) :
            comp_installed = False
            for _comp in comp:
                if _comp == "PrintRedir":
                    compstr = "Integrated Printing"
                else:
                    compstr = _comp
                if _comp in collected_data['agent']['Horizoncomp']:
                    if collected_data['agent']['Horizoncomp'][_comp] == 1:
                        comp_installed = True
                        s = "The VMware {} component is installed on the Horizon agent desktop. " \
                               "Please use it for {} redirection.".format(compstr,device.type)
                        suggestion.append(_add_refers(s,device.type,collected_data))
                        break
                else:
                    s = "The VMware {} component is not available in the Horizon agent product.".format(compstr)
                    suggestion.append(_add_refers(s,device.type,collected_data))
            if comp_installed == False :
                comp_string = " or ".join(comp)
                s = "The VMware {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp_string)
                error.append(_add_refers(s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            s = "The VMware {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp)
            error.append(_add_refers(s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 1:
            s = "The VMware {} component is installed on the Horizon agent desktop. " \
                               "Please use it for {} redirection.".format(comp,device.type)
            suggestion.append(_add_refers(s,device.type,collected_data))
        
    # todo: for different devices
    if device.type == 'usbdisk':
        error, warning, suggestion = _usb_disk_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'printers':
        error, warning, suggestion = _printer_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'scanners':
        error, warning, suggestion = _scanner_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'cameras':
        error, warning, suggestion = _camera_diagnose(collected_data, device, error, warning, suggestion)

    # todo: final check
    error = list(filter(None, error))
    warning = list(filter(None, warning))
    suggestion = list(filter(None, suggestion))

    return {'error': error,'warning': warning, 'suggestion': suggestion}


def _usb_disk_diagnose(collected_data, device, error, warning, suggestion):


    # todo: USB Arbitrator
    if collected_data['client'].get('USBArbitrator',None) == 'Stopped':
        error.append("Please check and ensure the USB arbitrator service is in running status on your client machine.")

    # todo: Redirection
    if device.is_usb_redirect:
        s = "You are using USB redirection for USB disk devices. Please use CDR redirection."
        error.append(_add_refers(s,device.type,collected_data))

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            s = "Please use the CDR (Client Drive Redirection) solution to redirect the file systems on USB disk devices."
            suggestion.append(_add_refers(s,'CDR',collected_data))
        else:
            s = "The CDR service is not running properly on your agent machine. Please check it with your IT administrator to restart the service."
            error.append(_add_refers(s,'CDR',collected_data))
    else:
        s = "The CDR component is not installed on your agent machine correctly. Please check it with your IT administrator."
    error.append(_add_refers(s,'CDR',collected_data))

    return error, warning, suggestion

def _printer_diagnose(collected_data, device, error, warning, suggestion):

    device_details = device.find_details()

    # todo: PrinterService
    s = "It is recommended to use printer redirection solution for this device in Horizon environment."
    suggestion.append(_add_refers(s,device.type,collected_data))

    if collected_data['client'].get('PrinterService',None) != 'Running':
        error.append("The print service(spooler) is not running on your client desktop."
                       "Please check it out and ensure it is running before printer redirection.")

    if collected_data['agent'].get('PrinterService',None) != 'Running':
        error.append("The print service(spooler) is not running on your agent desktop."
                       "Please check it out and ensure it is running before printer redirection.")

    if device.is_usb_redirect:
        error.append("You are using USB redirection for printer devices. Please use printer redirection.")
    
    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        if device.end == "client":
            conn = "connection"
        elif device.end == "agent":
            conn = "redirection"
        s = "This printer is connected to the Horizon {} machine via USB {}. " \
            "However, the device driver is not found in the machine. " \
            "Please contact IT administrator to install the printer driver in it.".format(device.end, conn)
        warning.append(s)

    else:
        # todo: check type 3 or type 4
        major_version= device_details['DriverName'].get('MajorVersion',None)
        if major_version == 3: # NPD
            agent_redirect =  device.find_redirection_in_agent()
            if agent_redirect is not None and agent_redirect['DriverName']['Name'] == 'VMware Universal EMF Driver':
                suggestion.append("VMware Universal Printing Driver(UPD) is used by this printer in remote desktop." \
                               " If you want to utilize Native Printing Driver(NPD), please install its native driver on the remote desktop.")
                # todo: update!


        elif major_version == 4: # UDPmajo
            pass

    return error, warning, suggestion

def _scanner_diagnose(collected_data, device, error, warning, suggestion):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    s = "It is recommended to use scanner redirection solution for this device in Horizon environment."
    suggestion.append(_add_refers(s,device.type,collected_data))

    if collected_data['client'].get('netlinkClientService',None) != 'Running':
        error.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your client desktop."
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['client'].get('scannerClientService',None) != 'Running':
        error.append("The VMware Scanner Redirection Client service(ftscanmgrhv) is not running on your client desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['agent'].get('netlinkAgentService',None) != 'Running':
        error.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your agent desktop."
                       "Please check it out and ensure it is running before scanner redirection.")

    if collected_data['agent'].get('scannerAgentService',None) != 'Running':
        error.append("The VMware Scanner Redirection Agent service(ftscansvchv) is not running on your agent desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['agent'].get('netlinkSessionService',None) != 'Running':
        error.append("The VMware Network Session service(ftnlses3hv) is not running on your agent desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")

    if device.is_usb_redirect:
        error.append("You are using USB redirection for scanner devices. Please use scanner redirection.")
    return error, warning, suggestion


def _camera_diagnose(collected_data, device, error, warning, suggestion):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    s = "It is recommended to use RTAV redirection solution for this device in Horizon environment."
    suggestion.append(_add_refers(s,device.type,collected_data))

    if collected_data['client'].get('audioService',None) != 'Running':
        error.append("The Windows Audio service(Audiosrv) is not running on your client desktop."
                       "Please check it out and ensure it is running before RTAV redirection.")
    
    if collected_data['agent'].get('audioService',None) != 'Running':
        error.append("The Windows Audio service(Audiosrv) is not running on your agent desktop."
                       "Please check it out and ensure it is running before RTAV redirection.")

    if device.is_usb_redirect:
        error.append("You are using USB redirection for camera devices. Please use RTAV redirection.")
    return error, warning, suggestion

def _other_diagnose(collected_data, device, error, warning, suggestion):
    return error, warning, suggestion

def _judge_driver(device):
    if "driverprovider" not in device.find_details().keys():
        return None
    provider = device.find_details()['driverprovider']
    if provider == 'Microsoft' \
        and re.search(r'.crosoft*',device.name) is None \
        and device.suspected_vendor is not 'Microsoft':
        return 'The driver is probably provided by Microsoft. Recommend to install the native driver provided by the device vendor.'
    return None


def _add_refers(suggestion,key,collected_data):
    if key not in docGUIDlinks.keys():
        return None
    prefix7="https://docs.vmware.com/en/VMware-Horizon-7/"
    prefix8="https://docs.vmware.com/en/VMware-Horizon/"
    middle="/horizon-remote-desktop-features/"
    horizon_ver=_get_horizon_ver(collected_data)
    if horizon_ver.startswith('7'):
        prefix= prefix7
        docver= horizon_ver
    else:
        prefix= prefix8
        #ToDo: check the agent version 2006 and build no
        docver= "2006"
    fulldoclink= prefix + docver  + middle + docGUIDlinks[key]
    return [suggestion, fulldoclink]

# Get the 7.13 as return value from agent version 7.13.0
def _get_horizon_ver(collected_data):
    version = collected_data['agent']['agentver']
    return '.'.join(version.split('.')[:-1])
