from util import *
import json
import re

components = {
    "usbdisk": "USB",
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
    results = []
    collected_data = collected_data

    # todo: general
    if device.has_problem:
        results.append("This device has some problems, please check.")
    if device.is_present == False:
        results.append("Please make sure this device is connected to your client machine by USB physically.")
    if device.is_reboot_needed:
        results.append("Please reboot your client machine OS to make this device work properly.")

    # todo: detect components in Horizon
    comp = components.get(device.type, None)
    if comp is not None:
        if isinstance(comp,list) :
            comp_installed = False
            for _comp in comp:
                 if _comp in collected_data['agent']['Horizoncomp']:
                    if collected_data['agent']['Horizoncomp'][_comp] == 1:
                        comp_installed = True
                        break
                 else:
                    s = "The {} component is not available in the Horizon agent product.".format(_comp)
                    results.append(_add_refers(s,device.type,collected_data))
            if comp_installed == False :
                comp_string = " or ".join(comp)
                s = "The {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp_string)
                results.append(_add_refers(s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            s = "The {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp)
            results.append(_add_refers(s,device.type,collected_data))

    # todo: for different devices
    if device.type == 'usbdisk':
        results = _usb_disk_diagnose(collected_data, device, results)
    elif device.type == 'printers':
        results = _printer_diagnose(collected_data, device, results)
    elif device.type == 'scanners':
        results = _scanner_diagnose(collected_data, device, results)
    elif device.type == 'cameras':
        results = _camera_diagnose(collected_data, device, results)

    # todo: final check
    results = list(filter(None, results))

    return results


def _usb_disk_diagnose(collected_data, device, results):


    # todo: USB Arbitrator
    if collected_data['client'].get('USBArbitrator',None) == 'Stopped':
        results.append("Please check and ensure the USB arbitrator service is in running status on your client machine.")

    # todo: Redirection
    if device.is_usb_redirect:
        s = "You are using USB redirection for USB disk devices. Please use CDR redirection."
        results.append(_add_refers(s,device.type,collected_data))

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            s = "Please use the CDR (client drive redirection) service to redirect the file systems on USB disk devices."
        else:
            s = "The CDR service is not running properly on your agent machine. Please check it with your IT administrator to restart the service."
    else:
        s = "The CDR component is not installed on your agent machine correctly. Please check it with your IT administrator."
    results.append(_add_refers(s,'CDR',collected_data))

    return results

def _printer_diagnose(collected_data, device, results):

    device_details = device.find_details()

    # todo: PrinterService
    s = "It is recommended to use printer redirection solution for this device in Horizon environment."
    results.append(_add_refers(s,device.type,collected_data))

    # Check which printer component is installed on agent
    if collected_data['agent']['Horizoncomp']['ThinPrint'] == 1:
        s = "The VMware ThinPrint component is installed on your agent machine. Please use it for printer redirection."
    elif collected_data['agent']['Horizoncomp']['PrintRedir'] == 1:
        s = "The VMware Integrated Printing component is installed on your agent machine. Please use it for printer redirection."
    results.append(s)

    if collected_data['client'].get('PrinterService',None) != 'Running':
        results.append("The print service(spooler) is not running on your client desktop."
                       "Please check it out and ensure it is running before printer redirection.")

    if collected_data['agent'].get('PrinterService',None) != 'Running':
        results.append("The print service(spooler) is not running on your agent desktop."
                       "Please check it out and ensure it is running before printer redirection.")

    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        s = "This printer  is connected to your machine via USB connection. " \
            "However, the appropriate driver of this device is not found in your client system. " \
            "Please contact your IT administrator to install the specific driver of the printer on your machine."
        results.append(s)

    else:
        # todo: check type 3 or type 4
        major_version= device_details['DriverName'].get('MajorVersion',None)
        if major_version == 3: # NPD
            agent_redirect =  device.find_redirection_in_agent()
            if agent_redirect is not None and agent_redirect['DriverName']['Name'] == 'VMware Universal EMF Driver':
                results.append("VMware Universal Printing Driver(UPD) is used by this printer in remote desktop." \
                               " If you want to utilize Native Printing Driver(NPD), please install its native driver on the remote desktop.")
                # todo: update!


        elif major_version == 4: # UDPmajo
            pass

    # todo： USB direction （vid & pid）or in _Device Class
    if device.is_usb_redirect:
        results.append("You are using USB redirection for printer devices. Please use printer redirection.")
        # todo : detect in agent
        if device.find_redirection_in_agent() is None:
            results.append("The USB redirection could not be found in Horizon end.")
    # else:
    #     results.append("It is a virtual printer.")

    return results

def _scanner_diagnose(collected_data, device, results):
    if _judge_driver(device) is not None:
        results.append(_judge_driver(device))
    s = "It is recommended to use scanner redirection solution for this device in Horizon environment."
    results.append(_add_refers(s,device.type,collected_data))

    if collected_data['client'].get('netlinkClientService',None) != 'Running':
        results.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your client desktop."
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['client'].get('scannerClientService',None) != 'Running':
        results.append("The VMware Scanner Redirection Client service(ftscanmgrhv) is not running on your client desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['agent'].get('netlinkAgentService',None) != 'Running':
        results.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your agent desktop."
                       "Please check it out and ensure it is running before scanner redirection.")

    if collected_data['agent'].get('scannerAgentService',None) != 'Running':
        results.append("The VMware Scanner Redirection Agent service(ftscansvchv) is not running on your agent desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['agent'].get('netlinkSessionService',None) != 'Running':
        results.append("The VMware Network Session service(ftnlses3hv) is not running on your agent desktop. "
                       "Please check it out and ensure it is running before scanner redirection.")

    if device.is_usb_redirect:
        results.append("You are using USB redirection for scanner devices. Please use scanner redirection.")
    return results


def _camera_diagnose(collected_data, device, results):
    if _judge_driver(device) is not None:
        results.append(_judge_driver(device))
    s = "It is recommended to use RTAV redirection solution for this device in Horizon environment."
    results.append(_add_refers(s,device.type,collected_data))

    if collected_data['client'].get('audioService',None) != 'Running':
        results.append("The Windows Audio service(Audiosrv) is not running on your client desktop."
                       "Please check it out and ensure it is running before RTAV redirection.")
    
    if collected_data['agent'].get('audioService',None) != 'Running':
        results.append("The Windows Audio service(Audiosrv) is not running on your agent desktop."
                       "Please check it out and ensure it is running before RTAV redirection.")

    if device.is_usb_redirect:
        results.append("You are using USB redirection for camera devices. Please use RTAV redirection.")
    return results


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
