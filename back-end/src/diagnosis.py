from util import *
import json

components = {
    "usbdisk": "USB",
    "printers": "ThinPrint"
}

link = {
    "CDR": ["https://docs.vmware.com/en/VMware-Horizon-7/",
            "/horizon-remote-desktop-features/GUID-25820640-60C2-4B7D-AE3F-F023E32B3DAE.html"],
    "usbdisk": ["https://docs.vmware.com/en/VMware-Horizon-7/",
                "/horizon-remote-desktop-features/GUID-777D266A-52C7-4C53-BAE2-BD514F4A800F.html"]
}


def diagnosis(collected_data, device):
    results = []
    end = device.end
    comp = components.get(device.type, None)
    # todo: general
    if device.has_problem:
        results.append("This device has some problems, please check.")

    if comp is not None and collected_data['agent']['Horizoncomp'][comp] == 0:
        results.append("Please install the {} component in Horizon client.".format(comp))

    if end == 'agent':
        results.append(["The redirection is not recommended for the {} device.".format(device.type),
                       link[device.type][0]+_get_Horizon_agent_version(collected_data)+link[device.type][1]])

    # todo: for different devices
    if device.type == 'usbdisk':
        results = _usb(collected_data, device, results)
    if device.type == 'printers':
        results = _printer(collected_data, device, results)

    return results


def _usb(collected_data, device, results):

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

    # todo: PrinterService (agent or client?)
    if collected_data['client'].get('PrinterService',None) != 'Running':
        results.append("Please start your Printer Service.")

    # todo: real printer or neetwork printer
    if device.vid is None and device.pid is None:
        results.append("Please use printer redirection.")

    return results

# questions：
# 如果检测到设备在client端运行 还需要要说  Please use CDR Service to redirect 么？

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
