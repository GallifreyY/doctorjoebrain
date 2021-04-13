# -*- coding: UTF-8 -*-
from util import *
import json
import re
from flask_babel import _


components = {
    "usbdisk": "ClientDriveRedirection",
    "virtualprinters": ["ThinPrint","PrintRedir"],
    "usbprinters": ["ThinPrint","PrintRedir"],
    "scanners": "ScannerRedirection",
    "cameras": "RTAV",
    "audio" : "RTAV",
    "smartcardreader" : "SmartCard"
}
TYPE_DICT = {
    "usbdisk": {"zh_cn": "USB硬盘", "en": "USB Disks","zh_tw":"USB磁盤"},
    "usbprinters": {"zh_cn": "USB打印机", "en": "USB Printers","zh_tw":"USB打印機"},
    "virtualprinters": {"zh_cn": "虚拟打印机", "en": "Virtual Printers","zh_tw":"虛擬打印機"},
    "scanners": {"zh_cn": "扫描仪", "en": "Scanners","zh_tw":"掃描儀"},
    "cameras": {"zh_cn": "摄像头", "en": "Cameras","zh_tw":"攝像頭"},
    "signaturepad": {"zh_cn": "签名板", "en": "Signature Pads","zh_tw":"簽名板"},
    "audio": {"zh_cn": "USB音箱", "en": "USB Audio","zh_tw":"USB音箱"},
    "speechmic": {"zh_cn": "USB语音麦克风", "en": "USB Speech Mics","zh_tw":"USB語音麥克風"},
    "barcodescanner": {"zh_cn": "USB扫码枪", "en": "USB Barcode Scanner","zh_tw":"USB掃碼槍"},
    "smartcardreader": {"zh_cn": "智能卡读卡器", "en": "Smartcard Reader","zh_tw":"智能卡讀卡器"},
    "others": {"zh_cn": "其它设备", "en": "Other Devices","zh_tw":"其他設備"}
}
docGUIDlinks = {
    "CDR": "GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html",
    "usbdisk": "GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html",
    "virtualprinters": "GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html",
    "usbprinters": "GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html",
    "scanners": "GUID-303F68FD-0CC1-4C9E-81ED-10C274669B93.html",
    "cameras": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html",
    "RTAV": "GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html",
    "SerialPort": "GUID-98B33D70-097E-419E-9B4D-7390E7CDF745.html",
    "RDSHsupported" : "GUID-35B4D247-C972-4C8F-8B13-326A01C0A245.html"
}

KBlinkIDs = {
    "CompositeSplit" : '2068447',
    'RDSH_RTAV' : '2148202'
}

def diagnosis_general_issues(collected_data):
    error = []
    warning = []
    suggestion = []
    collected_data = collected_data

    if collected_data['client'].get('clientService',None) != 'Running':
        trs_s=_("The VMware Horizon client service is not running on your client desktop. Please check it out and ensure it is running.")
        error.append(trs_s)
    if collected_data['agent'].get('agentService',None) != 'Running':
        trs_s=_("The VMware Horizon agent service is not running on your agent desktop. Please check it out and ensure it is running.")
        error.append(trs_s)
    if collected_data['client'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your client desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)
    if collected_data['agent'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)
    

    # Check the Desktop Experience component installation status on RDS
    if _is_agent_RDS(collected_data):
        if collected_data['agent'].get('DesktopExpInstalled',None) != True:
            trs_s = _("The Desktop Experience component is not installed on your RDS desktop. The VMware Horizon agent functions (such as scanner redirection) may not work normally because of it. Please check it out and ensure it is installed.")
            warning.append(trs_s)
        
    return {'error': error,'warning': warning,'suggestion':suggestion}

def diagnosis(collected_data, device,language):
    suggestion = []
    error = []
    warning = []
    collected_data = collected_data

    # todo: general
    if is_language_zh_cn(language):
        device_type = TYPE_DICT[device.type]['zh_cn']
    elif is_language_zh_tw(language):
        device_type = TYPE_DICT[device.type]['zh_tw']
    else:
        device_type = TYPE_DICT[device.type]['en']
    if device.problemcode!=None:
        if int(device.problemcode) > 0:
            trs_ss=_("This device has some configuration issues. The device problem code is %(problemcode)s. %(problemdesc)s",problemcode=device.problemcode,problemdesc=device.problemdesc)
            sslink = "https://support.microsoft.com/en-us/help/310123/error-codes-in-device-manager-in-windows"
            error.append([trs_ss,sslink])
    if device.is_present == False:
            trs=_("Please make sure this device is connected to your client machine by USB physically.")
            error.append(trs)
    if device.is_reboot_needed == True:
            trs=_("Please reboot your client machine OS to make this device work properly.")
            warning.append(trs)
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
                        trs_s=_("The VMware %(compstr)s component is installed on the Horizon agent desktop. Please use it for %(type)s redirection.",compstr=compstr,type=device_type)
                        suggestion.append(_add_refers(trs_s,device.type,collected_data,language))
                        break
                else:
                    trs_s=_("The VMware %(compstr)s component is not available in the current Horizon agent product version.",compstr=compstr)
                    suggestion.append(_add_refers(trs_s,device.type,collected_data,language))
            if comp_installed == False :
                comp_string = " or ".join(comp)
                trs_s=_("The VMware %(comp_string)s component is not installed on the Horizon agent desktop. Please check it with your IT administrator.",comp_string=comp_string)
                error.append(_add_refers(trs_s,device.type,collected_data,language))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            trs_s=_("The VMware %(comp)s component is not installed on the Horizon agent desktop. Please check it with your IT administrator.",comp=comp)
            error.append(_add_refers(trs_s,device.type,collected_data,language))
        elif collected_data['agent']['Horizoncomp'][comp] == 1:
            trs_s = _("The VMware %(comp)s component is installed on the Horizon agent desktop. Please use it for %(type)s redirection.",comp=comp,type=device_type)
            suggestion.append(_add_refers(trs_s, device.type, collected_data,language))
            if comp == "RTAV" and _is_agent_RDS(collected_data):
                trs_s=_("Please refer to this KB link for RTAV limitations on Windows Server OS.")
                suggestion.append(_add_KB_refers(trs_s,'RDSH_RTAV',language))
                
        
    # todo: for different devices
    if device.type == 'usbdisk':
        error, warning, suggestion = _usb_disk_diagnose(collected_data, device, error, warning, suggestion,language)
    elif device.type == 'virtualprinters' or device.type == 'usbprinters':
        error, warning, suggestion = _printer_diagnose(collected_data, device, error, warning, suggestion,language)
    elif device.type == 'scanners':
        error, warning, suggestion = _scanner_diagnose(collected_data, device,error, warning, suggestion,language)
    elif device.type == 'cameras':
        error, warning, suggestion = _camera_diagnose(collected_data, device, error, warning, suggestion,language)
    elif device.type == 'signaturepad':
        error, warning, suggestion = _signaturepad_diagnose(collected_data, device,error, warning, suggestion,language)
    elif device.type == 'speechmic':
        error, warning, suggestion = _speechmic_diagnose(collected_data, device, error, warning, suggestion,language)
    elif device.type == 'audio':
        error, warning, suggestion = _audio_diagnose(collected_data, device,error, warning, suggestion,language)
    elif device.type == 'barcodescanner':
        error, warning, suggestion = _barcode_diagnose(collected_data, device,error, warning, suggestion,language)
    elif device.type == 'smartcardreader':
        error, warning, suggestion = _smartcard_diagnose(collected_data, device,error, warning, suggestion,language)

    # todo: final check
    error = list(filter(None, error))
    warning = list(filter(None, warning))
    suggestion = list(filter(None, suggestion))

    return {'error': error,'warning': warning, 'suggestion': suggestion}


def _usb_disk_diagnose(collected_data, device,error, warning, suggestion,language):


    # todo: USB Arbitrator
    if collected_data['client'].get('USBArbitrator',None) == 'Stopped':
        trs_s=_("Please check and ensure the USB arbitrator service is in running status on your client machine.")
        error.append(trs_s)

    # todo: Redirection
    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for USB disk devices. Please use CDR redirection.")
        error.append(_add_refers(trs_s,device.type,collected_data,language))

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            trs_s=_("Please use the CDR (Client Drive Redirection) solution to redirect the file systems on USB disk devices.")
            suggestion.append(_add_refers(trs_s,'CDR',collected_data,language))
        else:
            trs_s=_("The CDR service is not running properly on your agent machine. Please check it with your IT administrator to restart the service.")
            error.append(_add_refers(trs_s,'CDR',collected_data,language))
    else:
        trs_s=_("The CDR component is not installed on your agent machine correctly. Please check it with your IT administrator.")
        error.append(_add_refers(trs_s,'CDR',collected_data,language))

    return error, warning, suggestion

def _printer_diagnose(collected_data, device,error, warning, suggestion,language):

    device_details = device.find_details()

    trs_s=_("It is recommended to use printer redirection solution for this device in Horizon environment.")
    suggestion.append(_add_refers(trs_s,device.type,collected_data,language))

    if collected_data['client'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your client desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)

    if collected_data['agent'].get('PrinterService',None) != 'Running':
        trs_s=_("The print service(spooler) is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
        error.append(trs_s)
    # Check printer service status for VMware Integrated Printing
    if _is_pr_installed(collected_data,"PrintRedir"):
        if collected_data['agent'].get('vmwareprintService',None) != 'Running':
                trs_s=_("The VMware print service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)
    # Check printer service status for VMware ThinPrint
    if _is_pr_installed(collected_data,"ThinPrint"):
        if collected_data['agent'].get('thinprintAutoConn',None) != 'Running':
                trs_s=_("The Thinprint AutoConnection service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)
        if collected_data['agent'].get('thinprintGateway',None) != 'Running':
                trs_s=_("The Thinprint Gateway service is not running on your agent desktop. Please check it out and ensure it is running before printer redirection.")
                error.append(trs_s)

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for printer devices. Please use printer redirection.")
        error.append(trs_s)

    if device.workoffline:
        trs_s=_("This printer is offline. Please check the device connection status firstly.")
        warning.append(trs_s)


    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        if device.end == "client":
            trs_conn=_("connection")
        elif device.end == "agent":
            trs_conn=_("redirection")
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
                # todo: update!


        elif major_version == 4: # UDPmajo
            pass

    return error, warning, suggestion

def _scanner_diagnose(collected_data, device,error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))

    trs_s=_("It is recommended to use scanner redirection solution for this device in Horizon environment.")
    suggestion.append(_add_refers(trs_s,device.type,collected_data,language))

    if collected_data['client'].get('netlinkClientService',None) != 'Running':
        trs_s=_("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your client desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)

    if collected_data['client'].get('scannerClientService',None) != 'Running':
        trs_s=_("The VMware Scanner Redirection Client service(ftscanmgrhv) is not running on your client desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)

    if collected_data['agent'].get('netlinkAgentService',None) != 'Running':
        trs_s=_("The VMware Netlink Supervisor service(ftnlsv3hv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)

    if collected_data['agent'].get('scannerAgentService',None) != 'Running':
        trs_s=_("The VMware Scanner Redirection Agent service(ftscansvchv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
        error.append(trs_s)

    if _is_below_HZN81(collected_data):
        if collected_data['agent'].get('netlinkSessionService',None) != 'Running':
            trs_s=_("The VMware Network Session service(ftnlses3hv) is not running on your agent desktop. Please check it out and ensure it is running before scanner redirection.")
            error.append(trs_s)

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for scanner devices. Please use scanner redirection.")
        error.append(trs_s)
    return error, warning, suggestion


def _camera_diagnose(collected_data, device, error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    
    trs_s=_("If this camera is a high resolution composite device, please contact your IT administrator for other solutions for it is not supported in Horizon yet.")
    suggestion.append(trs_s)

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for camera devices. Please use RTAV redirection.")
        error.append(trs_s)
    return error, warning, suggestion

def _signaturepad_diagnose(collected_data, device,error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    if device.name == "FT232R USB UART":
        # For Topaz BSB pad devices SerialPort
        trs_s=_("It is recommended to use Serial Port redirection solution for this device in Horizon environment.")
        suggestion.append(_add_refers(trs_s,'SerialPort',collected_data,language))
        if collected_data['agent']['Horizoncomp']['SerialPortRedirection'] == 0:
            trs_e=_("The VMware Serial Port redirection component is not installed on the Horizon agent desktop. Please check it with your IT administrator.")
            error.append(trs_e)
        elif collected_data['agent']['Horizoncomp']['SerialPortRedirection'] == 1:
            trs_s = _("The VMware Serial Port redirection component is installed on the Horizon agent desktop. Please use it for Topaz BSB signaturepad device redirection.")
            suggestion.append(trs_s)
        if collected_data['client'].get('serialClientService',None) != 'Running':
            trs_e=_("The VMware Serial Port redirection client service is not running on your client desktop. Please check it out and ensure it is running.")
            error.append(trs_e)
        if collected_data['agent'].get('serialAgentService',None) != 'Running':
            trs_e=_("The VMware Serial Port redirection agent service is not running on your agent desktop. Please check it out and ensure it is running.")
            error.append(trs_e)
        if device.is_usb_redirect:
            trs_e=_("You are using USB redirection for this device. Please use Serial Port redirection solution for it.")
            error.append(trs_e) 
    else:
        # For Non Topaz BSB pad devices and Wacom devices
        trs_s=_("It is recommended to use USB redirection solution for this device in Horizon environment.")
        suggestion.append(trs_s)
        if "STU-520" not in device.name  and _is_agent_RDS(collected_data):
            # Wacom 520 is the only supported signaturePad in RDSH by default
            trs_w=_("Horizon published RDS desktops and applications can only support \
                    a few USB devices. This device may be not supported by default.")
            warning.append(_add_refers(trs_w,"RDSHsupported",collected_data,language))            
    return error, warning, suggestion

def _USB_split_inc_policy_configed(collected_data, device):
    client_inc   = collected_data['client'].get('includVIDPID',None)
    client_split = collected_data['client'].get('splitVIDPID',None)
    agent_inc   = collected_data['agent'].get('includVIDPID',None)
    agent_split = collected_data['agent'].get('splitVIDPID',None)
    inc_pattern = "vid-" + str(device.vid) + "_pid-" + str(device.pid) 
    split_pattern = inc_pattern + "\(exintf:00;exintf:01;exintf:02.*\)"
    
    if (client_inc != None and client_split != None):
        if re.search(inc_pattern,client_inc) and re.search(split_pattern, client_split):
            return True
    elif (agent_inc != None and agent_split != None):
        if re.search(inc_pattern,agent_inc) and re.search(split_pattern, agent_split):
            return True
    else:
        return False

def _speechmic_diagnose(collected_data, device, error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))

    if "Windows" in collected_data['client'].get('OSname',None):
        # it is windows client
        if device.name == "PowerMicII-NS":
            audioExt=collected_data['client'].get('NuanceAudioExt',None)
            micExt=collected_data['client'].get('NuanceMicExt',None)
            trs_s=_("It is recommended to use Nuance extension solution for this device in Horizon environment.")
            powermiclink="https://dragonmedicalone.nuance.com/StandAlone/Production/DMO_AudioRouting_EN.pdf"
            suggestion.append([trs_s,powermiclink])
            if audioExt != None or micExt != None:
                # Nuance Extensions are fully or partially installed on client
                if audioExt != micExt:
                    trs_e=_("The Nuance VMware Client Audio extension version is %(audioExt)s while the Nuance PowerMic VMware client extension \
                            version is %(micExt)s. Please check and ensure they are of the same versions.",audioExt=audioExt,micExt=micExt)
                    error.append(trs_e)
                 
                if False == _USB_split_inc_policy_configed(collected_data, device):
                    if device.is_usb_redirect:
                        trs_e=_("You are using USB redirection for this device. Please use Nuance extension solution. \
                                 No need to redirect the device.")
                        error.append(trs_e)
                else:
                    trs_e=_("It is wrong to configure both USB split settings and Nuance extensions. \
                             Please contact your IT administrator to correct it.")
                    error.append(trs_e)
            else:
                # Nuance Extensions are not installed on client and USB split policy configured
                if True == _USB_split_inc_policy_configed(collected_data, device):
                    trs_s=_("The USB include and split policy are configured. Nuance Extensions are not installed on client. \
                             Use USB split with RTAV redirection solution for this device in Horizon environment.")
                    suggestion.append(_add_KB_refers(trs_s,'CompositeSplit',language))
                else:
                    trs_s=_("The USB include and split policy are not configured. Nuance Extensions are not installed on client. \
                            Please contact your IT administartor to configure Nuance extension solution for this device in Horizon environment.")
                    powermiclink="https://dragonmedicalone.nuance.com/StandAlone/Production/DMO_AudioRouting_EN.pdf"
                    suggestion.append([trs_s,powermiclink])
                    if device.is_usb_redirect:
                        trs_s=_("You are using pure USB redirection for this device. Please use Nuance extension solution or USB split with RTAV redirection solution.")
                        error.append(trs_s)
        else:
            # For other speech devices - Philips SpeechMike
            trs_s=_("It is recommended to use USB Split with RTAV redirection solution for this device in Horizon environment.")
            suggestion.append(_add_KB_refers(trs_s,'CompositeSplit',language))
            if False == _USB_split_inc_policy_configed(collected_data, device):
                trs_w=_("The USB include and split policy is not configured. Please contact your IT administrator to configure it correctly.")
                warning.append(trs_w)
    else:
        # For other horizon client platforms - linux client
        trs_s=_("It is recommended to use USB Split with RTAV redirection solution for this device in Horizon environment.")
        suggestion.append(_add_KB_refers(trs_s,'CompositeSplit',language))
        # Todo: to check the USB split policies on other horizon client platforms - linux client

    return error, warning, suggestion

def _audio_diagnose(collected_data, device, error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))

    if collected_data['client'].get('audioService',None) != 'Running':
        trs_s=_("The Windows Audio service(Audiosrv) is not running on your client desktop. Please check it out and ensure it is running before RTAV redirection.")
        error.append(trs_s)

    if collected_data['agent'].get('audioService',None) != 'Running':
        trs_s=_("The Windows Audio service(Audiosrv) is not running on your agent desktop. Please check it out and ensure it is running before RTAV redirection.")
        error.append(trs_s)

    if device.is_usb_redirect:
        trs_s=_("You are using USB redirection for audio devices. Please use RTAV redirection solution.")
        error.append(trs_s)
    return error, warning, suggestion

def _barcode_diagnose(collected_data, device,error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    trs_s=_("It is recommended to not do any redirection for this device in Horizon environment.")
    suggestion.append(trs_s)
    if device.is_usb_redirect:
        trs_e=_("You are using USB redirection for this device. Please leave it at client side. \
                 No need to do the USB redirection.")
        error.append(trs_e)
    return error, warning, suggestion

def _smartcard_diagnose(collected_data, device,error, warning, suggestion,language):
    if _judge_driver(device) is not None:
        warning.append(_judge_driver(device))
    trs_s=_("It is recommended to not do any redirection for this device in Horizon environment.")
    suggestion.append(trs_s)
    if device.is_usb_redirect:
        trs_e=_("You are using USB redirection for this device. Please leave it at client side. \
                 No need to do the USB redirection.")
        error.append(trs_e)
    return error, warning, suggestion

def _other_diagnose(collected_data, device,error, warning, suggestion,language):
    return error, warning, suggestion

def _judge_driver(device):
    if "driverprovider" not in device.find_details().keys():
        return None
    provider = device.find_details()['driverprovider']
    if provider == 'Microsoft' \
        and re.search(r'.crosoft*',str(device.name)) is None \
        and device.suspected_vendor != 'Microsoft':
        trs_s=_("The driver is probably provided by Microsoft. Recommend to install \
                 the native driver provided by the device vendor.")
        return trs_s
    return None

def _add_KB_refers(suggestion,key,language):
    if key not in KBlinkIDs.keys():
        return None
    prefix = "https://kb.vmware.com/s/article/"
    kbnumbers = KBlinkIDs[key]
    #Todo: may need to handle multiple KB links in future
    #Use the real language value
    if is_language_zh_cn(language) or is_language_zh_tw(language):
        lang = "zh_cn"
    else:
        lang = "en_us"
    fulldoclink = prefix + kbnumbers +"?lang=" + lang
    return [suggestion, fulldoclink]


def _add_refers(suggestion,key,collected_data,language):
    if key not in docGUIDlinks.keys():
        return None
    #Use the real language value
    if is_language_zh_cn(language):
        lang = "cn"
    elif is_language_zh_tw(language):
        lang = "tw"
    else:
        lang = "en"
    prefix7="https://docs.vmware.com/"+lang+"/VMware-Horizon-7/"
    prefix8="https://docs.vmware.com/"+lang+"/VMware-Horizon/"
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

