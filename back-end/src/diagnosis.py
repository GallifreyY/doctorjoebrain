from util import *
import json

components = {
    "usbdisk": "USB",
    "printers": ["ThinPrint","PrintRedir"]
}

link = {
    "CDR": ["https://docs.vmware.com/en/VMware-Horizon-7/",
            "/horizon-remote-desktop-features/GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html"],
    "usbdisk": ["https://docs.vmware.com/en/VMware-Horizon-7/",
                "/horizon-remote-desktop-features/GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html"]
}


def diagnosis(collected_data, device):
    results = []


    # todo: general
    if device.has_problem:
        results.append("This device has some problems, please check.")

    # todo: detect components in Horizon
    comp = components.get(device.type, None)
    if comp is not None:
        if isinstance(comp,list) :
            if _judge_comp([collected_data['agent']['Horizoncomp'][_comp] for _comp in comp]):
                comp_string = " or ".join(comp)
                results.append("Please install {} component in Horizon client.".format(comp_string))
        elif collected_data['agent']['Horizoncomp'][comp] == 0:
            results.append("Please install {} component in Horizon client.".format(comp))

    # todo: for different devices
    if device.type == 'usbdisk':
        results = _usb(collected_data, device, results)
    elif device.type == 'printers':
        results = _printer(collected_data, device, results)

    return results


def _usb(collected_data, device, results):

    # todo: Redirection
    if device.end == 'agent':
        results.append(["The redirection is not recommended for the {} device.".format(device.type),
                       link[device.type][0]+_get_Horizon_agent_version(collected_data)+link[device.type][1]])

    # todo: CDR Service
    if 'CDRservice' in collected_data['agent'].keys():
        cdr = []
        if collected_data['agent']['CDRservice'] == 'Running':
            cdr.append('Please use CDR Service to redirect the device.')
        else:
            cdr.append('Please restart your CDR Service.')
        cdr.append(link['CDR'][0] + _get_Horizon_agent_version(collected_data) + link['CDR'][1])
        results.append(cdr)
    else:
        pass  # add CDR?
    return results

def _printer(collected_data, device, results):

    device_details = device.find_details_in(collected_data)

    # todo：installed driver
    if 'DriverName' not in device_details.keys():
        results.append("Please install according printer drivers")

    else:
        # todo: check type 3 or type 4
        major_version= device_details['DriverName'].get('MajorVersion',None)
        if major_version == 3: # NPD
            agent_redirect =  device.find_redirection_in_agent(collected_data)
            if agent_redirect is not None and agent_redirect['DriverName']['Name'] == 'Vmware.. ':
                results.append("Only can conduct UDP Service")
                # todo: update!
                #  It must has driver?

        elif major_version == 4: # UDP
            pass

    # todo： USB direction （vid & pid）or in _Device Class
    if device.is_usb_redirect():
        results.append("Not recommending using USB redirect in this printer device, please use printer redirection.")
        # todo : detect in agent
        if  device.find_redirection_in_agent(collected_data) is not None:
            results.append("The USB redirection could not be found in Horizon end.")
    else:
        results.append("It is a virtual printer.")


    # todo: PrinterService
    if collected_data['client'].get('PrinterService',None) != 'Running':
        results.append("Please start your Printer Service at localhost.")

    if collected_data['agent'].get('PrinterService',None) != 'Running':
        results.append("Please start your Printer Service at Horizon Agent.")

    return results



def _get_Horizon_agent_version(collected_data):
    version = collected_data['agent']['agentver']
    # todo: seconding version
    return '.'.join(version.split('.')[:-1])

def _judge_comp(comp_list):
    for comp in comp_list:
        if comp == 1:
            return False
    return True

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
