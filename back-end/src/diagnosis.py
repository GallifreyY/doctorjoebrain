from util import *
import json

components = {
    "usbdisk": "USB"
}

suggestions = {
    "general": {
        "comp": "Please install the xxx component in Horizon client",
        "redirect": "The redirection is not recommended for this device"
    },
    "usbdisk": {
    }
}


def diagnosis(collected_data, device):
    results = []
    end = device.end
    comp = components.get(device.type, None)
    # todo: general
    if device.has_problem:
        results.append("This device has some problems, please check.")

    if comp is not None and collected_data['agent']['Horizoncomp'][comp] == 0:
        results.append("Please install the {} component in Horizon client".format(comp))

    if end == 'agent':
        results.append(suggestions['general']['redirect'])

    # todo: for different devices
    if device.type == 'usbdisk':
        results = _usb(collected_data, end, results)

    return results


def _usb(collected_data, device, results):
    # todo: 设备本身有问题
    if 'CDRservice' in collected_data['agent'].keys():
        if collected_data['agent']['CDRservice'] == 'Running':
            results.append('Please use CDR Service to redirect the device')
        else:
            results.append('Please restart your CDR Service')
    else:
        pass  # add CDR?
    return results

# questions：
# 如果检测到设备在client端运行 还需要要说  Please use CDR Service to redirect 么？


# todo：test

# uuid = 'test'
# collected_data = locate_json(uuid)
# device = 'usbdisk'
# print(diagnosis(collected_data, device))

