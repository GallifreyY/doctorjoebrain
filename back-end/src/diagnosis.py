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
    end = recognize_end(collected_data, device)
    comp = components.get(device, None)
    print(comp)
    # todo: general
    if comp is not None and collected_data['agent']['Horizoncomp'][comp] == 0:
        results.append("Please install the {} component in Horizon client".format(comp))

    if end == 'agent':
        results.append(suggestions['general']['redirect'])

    # todo: for different devices
    if device == 'usbdisk':
        results = _usb(collected_data, results)

    return results


def _usb(collected_data, results):
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

