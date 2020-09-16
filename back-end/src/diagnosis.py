from util import *
import json
import re

components = {
    "usbdisk": "USB",
    "printers": ["ThinPrint","PrintRedir"]
}

link = {
    "CDR": ["https://docs.vmware.com/en/VMware-Horizon-7/",
            "/horizon-remote-desktop-features/GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html"],
    "usbdisk": ["https://docs.vmware.com/en/VMware-Horizon-7/",
                "/horizon-remote-desktop-features/GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html"],
    "printer_redirection":["https://docs.vmware.com/en/VMware-Horizon-7/",
                "/horizon-remote-desktop-features/GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html"]
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
                               "Please install it on your remote desktop".format(comp_string)
                results.append(_add_refers(s,device.type,collected_data))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            s = "The {} component is not installed on the Horizon agent desktop. " \
                               "Please install it on your remote desktop".format(comp)
            results.append(_add_refers(s,device.type,collected_data))

    # todo: for different devices
    if device.type == 'usbdisk':
        results = _usb_diagnose(collected_data, device, results)
    elif device.type == 'printers':
        results = _printer_diagnose(collected_data, device, results)
    elif device.type == 'scanners':
        results = _scanner_diagnose(collected_data, device, results)
    elif device.type == 'cameras':
        results = _camera_diagnose(collected_data, device, results)

    # todo: final check
    results = list(filter(None, results))

    return results


def _usb_diagnose(collected_data, device, results):


    # todo: USB Arbitrator
    if collected_data['client'].get('USBArbitrator',None) == 'Stopped':
        results.append("Please check and ensure the USB arbitrator service is in running status on your client machine.")

    # todo: Redirection
    if device.end == 'agent':
        s = "The USB device  is redirected to the remote agent desktop by USB redirection way which is not recommended for the USB disk devices."
        results.append(_add_refers(s,device.type,collected_data))

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            s = "Please use the CDR (client drive redirection) service to redirect the file systems on USB disk devices."
        else:
            s = "The CDR service was not running properly on your agent machine. Please check it with your IT administrator to restart the service."
    else:
        s = "The CDR component was not installed on your remote agent desktop correctly. Please check it with your IT administrator."
    results.append(_add_refers(s,'CDR',collected_data))

    return results

def _printer_diagnose(collected_data, device, results):

    device_details = device.find_details()

    # todo: PrinterService
    s = "It is recommended to use Printer redirection solution for this device in Horizon environment."
    results.append(_add_refers(s,"printer_redirection",collected_data))


    if collected_data['client'].get('PrinterService',None) != 'Running'\
            or collected_data['agent'].get('PrinterService',None) != 'Running':
        results.append("The print service(spooler) was at stopped status on your client or agent desktop. "
                       "Please check it out and ensure it is running before printer redirection..")
        return results

    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        s = "This printer  is connected to your machine via USB connection. " \
            "However, the appropriate driver of this device was not found in your client system. " \
            "Please contact your IT administrator to install the specific driver of the printer on your machine."
        results.append(s)

    else:
        # todo: check type 3 or type 4
        major_version= device_details['DriverName'].get('MajorVersion',None)
        if major_version == 3: # NPD
            agent_redirect =  device.find_redirection_in_agent()
            if agent_redirect is not None and agent_redirect['DriverName']['Name'] == 'VMware Universal EMF Driver':
                results.append("VMware Universal Printing Driver(UPD) was used by this printer in remote desktop." \
                               " If you want to utilize Native Printing Driver(NPD), please install its native driver on the remote desktop.")
                # todo: update!


        elif major_version == 4: # UDPmajo
            pass

    # todo： USB direction （vid & pid）or in _Device Class
    if device.is_usb_redirect:
        results.append("Not recommend using USB redirect in this printer device, please use printer redirection.")
        # todo : detect in agent
        if device.find_redirection_in_agent() is None:
            results.append("The USB redirection could not be found in Horizon end.")
    # else:
    #     results.append("It is a virtual printer.")

    return results

def _scanner_diagnose(collected_data, device, results):
    if _judge_driver(device) is not None:
        results.append(_judge_driver(device))

    return results


def _camera_diagnose(collected_data, device, results):
    if _judge_driver(device) is not None:
        results.append(_judge_driver(device))

    return results


def _judge_driver(device):
    if "driverprovider" not in device.find_details().keys():
        return None
    provider = device.find_details()['driverprovider']
    if provider == 'Microsoft' \
        and re.search(r'.crosoft*',device.name) is None \
        and device.suspected_vendor is not 'Microsoft':
        return 'The driver is probably provided by Microsoft. Recommend to install the driver from the vendor.'
    return None

def _add_refers(suggestion,key,collected_data):
    if key not in link.keys():
        return None
    return [suggestion,
            link[key][0] + _get_Horizon_agent_version(collected_data) + link[key][1]]


def _get_Horizon_agent_version(collected_data):
    version = collected_data['agent']['agentver']
    # todo: seconding version
    return '.'.join(version.split('.')[:-1])

# todo：test
#
# uuid = '25633f65-f820-40c6-b725-179fdbf74621'
# collected_data = read_data(uuid)
# print(_get_Horizon_agent_version(collected_data))
# device = read_data(uuid, 'devices', 'pickle')[0]
# print(diagnosis(collected_data, device))

# link
# CDR 的 -  https://docs.vmware.com/en/VMware-Horizon-7/7.10/horizon-remote-desktop-features/GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html
# USB的- https://docs.vmware.com/en/VMware-Horizon-7/7.10/horizon-remote-desktop-features/GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html
# Printer 的 -  https://docs.vmware.com/en/VMware-Horizon-7/7.10/horizon-remote-desktop-features/GUID-39C87770-69C9-4EEF-BBDB-8ED5C0705611.html
# Scanner -  https://docs.vmware.com/en/VMware-Horizon-7/7.10/horizon-remote-desktop-features/GUID-303F68FD-0CC1-4C9E-81ED-10C274669B93.html
# RTAV - https://docs.vmware.com/en/VMware-Horizon-7/7.10/horizon-remote-desktop-features/GUID-D6FD6AD1-D326-4387-A6F0-152C7D844AA0.html
