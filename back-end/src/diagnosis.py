# -*- coding: UTF-8 -*-
from util import *
import json
import re
from flask_babel import _
# _ = None
# def getUserLanguage():
#     return "zh"
#
# # Get loc string by language
# def getLocStrings():
#     currentDir = os.path.dirname(os.path.realpath(__file__))
#     print(currentDir)
#     return gettext.translation('messages', currentDir, [getUserLanguage(), "zh"]).gettext
#
# _ = getLocStrings()

components = {
    "usbdisk": "ClientDriveRedirection",
    "virtualprinters": ["ThinPrint","PrintRedir"],
    "usbprinters": ["ThinPrint","PrintRedir"],
    "scanners": "ScannerRedirection",
    "cameras": "RTAV"
}

docGUIDlinks = {
    "CDR": "GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html",
    "usbdisk": "GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html",
    "virtualprinters": "GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html",
    "usbprinters": "GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html",
    "scanners": "GUID-303F68FD-0CC1-4C9E-81ED-10C274669B93.html",
    "cameras": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html",
    "RTAV": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html"
}

def diagnosis_general_issues(collected_data):
    error = []
    warning = []
    collected_data = collected_data

    if collected_data['client'].get('clientService',None) != 'Running':
        error.append("The VMware Horizon client service is not running on your client desktop."
                       "Please check it out and ensure it is running.")

    if collected_data['agent'].get('agentService',None) != 'Running':
        error.append("The VMware Horizon agent service is not running on your agent desktop."
                       "Please check it out and ensure it is running.")

    # Check the Desktop Experience component installation status on RDS
    if _is_agent_RDS(collected_data):
        if collected_data['agent'].get('DesktopExpInstalled',None) != True:
            warning.append("The Desktop Experience component is not installed on your RDS desktop."
                        "The VMware Horizon agent functions (such as scanner redirection) may not work normally because of it."
                        "Please check it out and ensure it is installed.")
        
    return {'error': error,'warning': warning}

def diagnosis(collected_data, device):
    suggestion = []
    error = []
    warning = []
    collected_data = collected_data

    # todo: general
    if device.problemcode!=None:
        if int(device.problemcode) > 0:
            ss="This device has some configuration issues. The device problem code is {}. {}".format(device.problemcode, device.problemdesc)
            trs_ss=_("This device has some configuration issues. The device problem code is %(problemcode)s. %(problemdesc)s",problemcode=device.problemcode,problemdesc=device.problemdesc)
            sslink = "https://support.microsoft.com/en-us/help/310123/error-codes-in-device-manager-in-windows"
            error.append([trs_ss,sslink])
    if device.is_present == False:
            trs=_("Please make sure this device is connected to your client machine by USB physically.")
            #error.append("Please make sure this device is connected to your client machine by USB physically.")
            error.append(trs)
    if device.is_reboot_needed == True:
            trs=_("Please reboot your client machine OS to make this device work properly.")
            #warning.append("Please reboot your client machine OS to make this device work properly.")
            warning.append(trs)
    # todo: detect components in Horizon
    comp = components.get(device.type, None)
    if comp is not None:
        if isinstance(comp,list) :
            comp_installed = False
            for _comp in comp:
                if _comp == "PrintRedir":
                    compstr = "Integrated Printing"
                    comtrs_str = _("Integrated Printing")
                else:
                    compstr = _comp
                if _comp in collected_data['agent']['Horizoncomp']:
                    if collected_data['agent']['Horizoncomp'][_comp] == 1:
                        comp_installed = True
                        s = "The VMware {} component is installed on the Horizon agent desktop. " \
                               "Please use it for {} redirection.".format(compstr,device.type)
                        trs_s=_("The VMware %(compstr)s component is installed on the Horizon agent desktop. Please use it for %(type)s redirection.",compstr=compstr,type=device.type)
                        suggestion.append(_add_refers(trs_s,device.type,collected_data))
                        break
                else:
                    s = "The VMware {} component is not available in the Horizon agent product.".format(compstr)
                    trs_s=_("The VMware %(compstr)s component is not available in the Horizon agent product.",compstr=compstr)
                    suggestion.append(_add_refers(trs_s,device.type,collected_data))
            if comp_installed == False :
                comp_string = " or ".join(comp)
                s = "The VMware {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp_string)
                trs_s=_("The VMware %(comp_string)s component is not installed on the Horizon agent desktop. Please check it with your IT administrator.",comp_string=comp_string)
                error.append(_add_refers(trs_s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            s = "The VMware {} component is not installed on the Horizon agent desktop. " \
                               "Please check it with your IT administrator.".format(comp)
            trs_s=_("The VMware %(comp)s component is not installed on the Horizon agent desktop. Please check it with your IT administrator.",comp=comp)
            error.append(_add_refers(trs_s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 1:
            s = "The VMware {} component is installed on the Horizon agent desktop. " \
                               "Please use it for {} redirection.".format(comp,device.type)
            trs_s = _("The VMware %(comp)s component is installed on the Horizon agent desktop. Please use it for %(type)s redirection.",comp=comp,type=device.type)
            #suggestion.append(_add_refers(s,device.type,collected_data))
            suggestion.append(_add_refers(trs_s, device.type, collected_data))
        
    # todo: for different devices
    if device.type == 'usbdisk':
        error, warning, suggestion = _usb_disk_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'virtualprinters' or device.type == 'usbprinters':
        error, warning, suggestion = _printer_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'scanners':
        error, warning, suggestion = _scanner_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'cameras':
        error, warning, suggestion = _camera_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'signaturepad':
        error, warning, suggestion = _signaturepad_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'speechmic':
        error, warning, suggestion = _speechmic_diagnose(collected_data, device, error, warning, suggestion)
    elif device.type == 'audio':
        error, warning, suggestion = _audio_diagnose(collected_data, device, error, warning, suggestion)

    # todo: final check
    error = list(filter(None, error))
    warning = list(filter(None, warning))
    suggestion = list(filter(None, suggestion))

    return {'error': error,'warning': warning, 'suggestion': suggestion}


def _usb_disk_diagnose(collected_data, device, error, warning, suggestion):


    # todo: USB Arbitrator
    if collected_data['client'].get('USBArbitrator',None) == 'Stopped':
        trs_s=_("Please check and ensure the USB arbitrator service is in running status on your client machine.")
        error.append(trs_s)
        #error.append("Please check and ensure the USB arbitrator service is in running status on your client machine.")

    # todo: Redirection
    if device.is_usb_redirect:
        s = "You are using USB redirection for USB disk devices. Please use CDR redirection."
        trs_s=_("You are using USB redirection for USB disk devices. Please use CDR redirection.")
        error.append(_add_refers(trs_s,device.type,collected_data))

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            s = "Please use the CDR (Client Drive Redirection) solution to redirect the file systems on USB disk devices."
            trs_s=_("Please use the CDR (Client Drive Redirection) solution to redirect the file systems on USB disk devices.")
            suggestion.append(_add_refers(trs_s,'CDR',collected_data))
        else:
            s = "The CDR service is not running properly on your agent machine. Please check it with your IT administrator to restart the service."
            trs_s=_("The CDR service is not running properly on your agent machine. Please check it with your IT administrator to restart the service.")
            error.append(_add_refers(trs_s,'CDR',collected_data))
    else:
        s = "The CDR component is not installed on your agent machine correctly. Please check it with your IT administrator."
        trs_s=_("The CDR component is not installed on your agent machine correctly. Please check it with your IT administrator.")
        error.append(_add_refers(trs_s,'CDR',collected_data))

    return error, warning, suggestion

def _printer_diagnose(collected_data, device, error, warning, suggestion):

    device_details = device.find_details()

    # todo: PrinterService
    s = "It is recommended to use printer redirection solution for this device in Horizon environment."
    trs_s=_("It is recommended to use printer redirection solution for this device in Horizon environment.")
    suggestion.append(_add_refers(trs_s,device.type,collected_data))

    if collected_data['client'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your client desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)
        #error.append("The print service(spooler) is not running on your client desktop."
                      # "Please check it out and ensure it is running before printer redirection.")

    if collected_data['agent'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)
        # error.append("The print service(spooler) is not running on your agent desktop."
        #                "Please check it out and ensure it is running before printer redirection.")
    # Check printer service status for VMware Integrated Printing
    if _is_pr_installed(collected_data,"PrintRedir"):
        if collected_data['agent'].get('vmwareprintService',None) != 'Running':
                trs_s=_("The VMware print service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                # error.append("The VMware print service is not running on your agent desktop."
                #             "Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)
    # Check printer service status for VMware ThinPrint
    if _is_pr_installed(collected_data,"ThinPrint"):
        if collected_data['agent'].get('thinprintAutoConn',None) != 'Running':
                trs_s=_("The Thinprint AutoConnection service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)
                # error.append("The Thinprint AutoConnection service is not running on your agent desktop."
                #             "Please check it out and ensure it is running before printer redirection.")
        if collected_data['agent'].get('thinprintGateway',None) != 'Running':
                trs_s=_("The Thinprint Gateway service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)
                # error.append("The Thinprint Gateway service is not running on your agent desktop."
                #             "Please check it out and ensure it is running before printer redirection.")

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for printer devices. Please use printer redirection.")
        error.append(trs_s)
        # error.append("You are using USB redirection for printer devices. Please use printer redirection.")
    
    if device.workoffline:
        trs_s=_("This printer is offline. Please check the device connection status firstly.")
        warning.append(trs_s)
        # warning.append("This printer is offline. Please check the device connection status firstly.")


    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        if device.end == "client":
            conn = "connection"
            trs_conn=_("connection")
        elif device.end == "agent":
            conn = "redirection"
            trs_conn=_("redirection")
        s = "This printer is connected to the Horizon {} machine via USB {}. " \
            "However, the device driver is not found in the machine. " \
            "Please contact IT administrator to install the printer driver in it.".format(device.end, conn)
        trs_s=_("This printer is connected to the Horizon %(end)s machine via USB %(trs_conn)s. However, the device driver is not found in the machine. Please contact IT administrator to install the printer driver in it.",\
                end=device.end,trs_conn=trs_conn)
        warning.append(trs_s)

    else:
        # todo: check type 3 or type 4
        major_version= device_details['DriverName'].get('MajorVersion',None)
        if major_version == 3: # NPD
            agent_redirect =  device.find_redirection_in_agent()
            if agent_redirect is not None and agent_redirect['DriverName']['Name'] == 'VMware Universal EMF Driver':
                trs_s=_("VMware Universal Printing Driver(UPD) is used by this printer in remote desktop. If you want to utilize Native Printing Driver(NPD), please install its native driver on the remote desktop.")
                suggestion.append(trs_s)
                # suggestion.append("VMware Universal Printing Driver(UPD) is used by this printer in remote desktop." \
                #                " If you want to utilize Native Printing Driver(NPD), please install its native driver on the remote desktop.")
                # todo: update!


        elif major_version == 4: # UDPmajo
            pass

    return error, warning, suggestion

def _scanner_diagnose(collected_data, device, error, warning, suggestion):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    s = "It is recommended to use scanner redirection solution for this device in Horizon environment."
    trs_s=_("It is recommended to use scanner redirection solution for this device in Horizon environment.")
    suggestion.append(_add_refers(trs_s,device.type,collected_data))

    if collected_data['client'].get('netlinkClientService',None) != 'Running':
        trs_s=_("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your client desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)
        # error.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your client desktop."
        #                "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['client'].get('scannerClientService',None) != 'Running':
        trs_s=_("The VMware Scanner Redirection Client service(ftscanmgrhv) is not running on your client desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)
        # error.append("The VMware Scanner Redirection Client service(ftscanmgrhv) is not running on your client desktop. "
        #                "Please check it out and ensure it is running before scanner redirection.")
    
    if collected_data['agent'].get('netlinkAgentService',None) != 'Running':
        trs_s=_("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)
        # error.append("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your agent desktop."
        #                "Please check it out and ensure it is running before scanner redirection.")

    if collected_data['agent'].get('scannerAgentService',None) != 'Running':
        trs_s=_("The VMware Scanner Redirection Agent service(ftscansvchv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)
        # error.append("The VMware Scanner Redirection Agent service(ftscansvchv) is not running on your agent desktop. "
        #                "Please check it out and ensure it is running before scanner redirection.")
    
    if _is_below_HZN81(collected_data):
        if collected_data['agent'].get('netlinkSessionService',None) != 'Running':
            trs_s=_("The VMware Network Session service(ftnlses3hv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
            error.append(trs_s)
            # error.append("The VMware Network Session service(ftnlses3hv) is not running on your agent desktop. "
            #               "Please check it out and ensure it is running before scanner redirection.")

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for scanner devices. Please use scanner redirection.")
        error.append(trs_s)
        # error.append("You are using USB redirection for scanner devices. Please use scanner redirection.")
    return error, warning, suggestion


def _camera_diagnose(collected_data, device, error, warning, suggestion):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    s = "It is recommended to use RTAV redirection solution for this device in Horizon environment."
    trs_s=_("It is recommended to use RTAV redirection solution for this device in Horizon environment.")
    suggestion.append(_add_refers(trs_s,device.type,collected_data))

    if collected_data['client'].get('audioService',None) != 'Running':
        trs_s=_("The Windows Audio service(Audiosrv) is not running on your client desktop. Please check it out and ensure it is running before RTAV redirection.")
        error.append(trs_s)
        # error.append("The Windows Audio service(Audiosrv) is not running on your client desktop."
        #                "Please check it out and ensure it is running before RTAV redirection.")
    
    if collected_data['agent'].get('audioService',None) != 'Running':
        trs_s=_("The Windows Audio service(Audiosrv) is not running on your agent desktop. Please check it out and ensure it is running before RTAV redirection.")
        error.append(trs_s)
        # error.append("The Windows Audio service(Audiosrv) is not running on your agent desktop."
        #                "Please check it out and ensure it is running before RTAV redirection.")

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for camera devices. Please use RTAV redirection.")
        error.append(trs_s)
        # error.append("You are using USB redirection for camera devices. Please use RTAV redirection.")
    return error, warning, suggestion

def _signaturepad_diagnose(collected_data, device, error, warning, suggestion):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    return error, warning, suggestion

def _speechmic_diagnose(collected_data, device, error, warning, suggestion):
    return error, warning, suggestion

def _audio_diagnose(collected_data, device, error, warning, suggestion):
    return error, warning, suggestion

def _other_diagnose(collected_data, device, error, warning, suggestion):
    return error, warning, suggestion

def _judge_driver(device):
    if "driverprovider" not in device.find_details().keys():
        return None
    provider = device.find_details()['driverprovider']
    if provider == 'Microsoft' \
        and re.search(r'.crosoft*',str(device.name)) is None \
        and device.suspected_vendor is not 'Microsoft':
        trs_s=_("The driver is probably provided by Microsoft. Recommend to install the native driver provided by the device vendor.")
        return trs_s
        # return 'The driver is probably provided by Microsoft. Recommend to install the native driver provided by the device vendor.'
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
        # The agent doc version is like 2006 , 2012, etc.
        if 'agentdocver' in collected_data['agent']:
            if collected_data['agent']['agentdocver'] is not None:
                docver = collected_data['agent']['agentdocver']
            else:
                docver = "2006" # Add a default value as Horizon 8.0(2006)
        else:
            docver = "2006" # Add a default value as Horizon 8.0(2006)
    fulldoclink= prefix + docver  + middle + docGUIDlinks[key]
    return [suggestion, fulldoclink]

# Get the 7.13 as return value from agent version 7.13.0
def _get_horizon_ver(collected_data):
    version = collected_data['agent']['agentver']
    return '.'.join(version.split('.')[:-1])

# HZN version is less than version 8.1.0
def _is_below_HZN81(collected_data):
    version = collected_data['agent']['agentver']
    major = int((version.split('.'))[0])
    minor = int((version.split('.'))[1])
    if (major < 8 or (major == 8 and minor == 0)):
        return True
    else:
        return False

# Check if HZN agent is server OS
def _is_agent_RDS(collected_data):
    osname = collected_data['agent']['OSname']
    if ('Server' in osname):
        return True
    else:
        return False

# Check if Printer redirection component is installed or not
# pr - PrintRedir  or ThinPrint
def _is_pr_installed(collected_data,pr):
     #check thinprint/vmwareprint 
    details = collected_data['agent'].get('Horizoncomp', None)
    if details != None:
        prvalue = details.get(pr, None)
        if prvalue is not None:
            if int(prvalue) == 1:
                return True
    return False
