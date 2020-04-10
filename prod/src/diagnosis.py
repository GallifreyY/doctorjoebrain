from util import *
import json

components = {
    "usbdisk": "USB"
}


def diagnosis(collected_data, device):
    results = []
    comp = components.get(device, None)

    # todo：where device is in, agent or client
    end = recognize_end(collected_data, device)

    # todo: general check
    if comp is not None and collected_data['agent']['Horizoncomp'][comp] == 0:
        results.append("Please install the {} component in Horizon client".format(comp))

    if end == 'agent':
        results.append("The redirection is not recommended for this device")

    # todo: usb check
    if device == 'usbdisk':
        results = _usb(collected_data, results)

    return results


def _usb(collected_data, results):
    if 'CDRservice' in collected_data['agent'].keys():
        results.append('Please use CDR Service to redirect the device')
        if collected_data['agent']['CDRservice'] != 'Running':
            results.append('Please restart your CDR Service')
    else:
        pass  # add CDR?
    return results

# todo：test

# uuid = 'test'
# collected_data = locate_json(uuid)
# device = 'usbdisk'
# print(diagnosis(collected_data, device))
