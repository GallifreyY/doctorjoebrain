import json
import sys
import os
import random
import json
import datetime
import requests
import string

# todo: read horizon components data
with open("./lib/Horizon_components.json", "r") as f:
    Horizon_components = json.load(f)

# todo : read virtual pritners data
with open("./lib/virtual_printers.json", "r") as f:
    vp = json.load(f)
virtual_printer_client = vp["client"]
virtual_printer_agent = vp["agent"]


class Mock():
    def __init__(self):

        self.data = {"code": 20022,
                     "data": {
                         "client": {
                             "OSname": "Windows 10",
                             "OSver": "1909",
                             "clientver": "8.0.0.11085",
                             "PrinterService": "Running",
                             "USBArbitrator": "Running",
                             "usbdisk": None,
                             "printers": None
                         }, "agent": {
                             "OSname": "Windows 10",
                             "OSver": "1909",
                             "agentver": "7.12.0",
                             "Horizoncomp": Horizon_components,
                             "CDRservice": "Running",
                             "PrinterService": "Running",
                             "usbdisk": None,
                             "printers": None
                         }}}

    def update_attribute(self,end='client',**kw):

        for key in kw.keys():
            if key in self.data['data'][end].keys():
                self.data['data'][end][key] = kw[key]

    def update_Horizon_comp(self, **kw):

        for key in kw.keys():
            if key in self.data['data']['agent']['Horizoncomp']:
                self.data['data']['agent']['Horizoncomp'][key] = kw[key]


    def info(self): print(self.data)


    def generate_device(self, d_type='USB', end='client', is_id_fixed=False, **kw):

        devices = {'USB': 'usbdisk',
                   'PRINTER': 'printers'}

        if not d_type in devices.keys():
            print("this device type could not be generated")
            return None
        else:
            type = devices[d_type]

        if self.data["data"][end][type] is None:
            self.data["data"][end][type] = []

        vid = "1E3D" if is_id_fixed else str(random.randrange(1000, 9999))
        pid = "2096" if is_id_fixed else str(random.randrange(1000, 9999))


        if type == 'usbdisk':

            name = "USB Mass Storage Device" \
                if is_id_fixed \
                else "USB_" + "".join(random.sample(string.ascii_letters + string.digits, 5))

            device = {
                "VID": vid,
                "PID": pid,
                "manufacturer": "Compatible USB storage device",
                "name": name,
                "vendor": "Generic",
                "product": "Flash_Disk",
                "driverprovider": "Microsoft",
                "driverver": "10.0.18362.1",
                "isRebootNeeded": False,
                "isPresent": True,
                "hasProblem": False
            }

        elif type == 'printers':
            name = "Brother QL-720NW" \
                if is_id_fixed \
                else "Pinter_" + "".join(random.sample(string.ascii_letters + string.digits, 5))

            device = {
                "Name": name,
                "DriverName": {
                    "Name": "Brother QL-720NW",
                    "MajorVersion": 3,
                    "Manufacturer": "Brother",
                    "DriverVersion": "6.5.0.7"
                },
                "Default": False,
                "location": None,
                "Local": True,
                "Network": False,
                "DeviceID": "Brother QL-720NW",
                "Printerstatus": 3,
                "Printerstate": 0,
                "VID": vid,
                "PID": pid,
                "isRebootNeeded": False,
                "isPresent": True,
                "hasProblem": False
            }

        for key in kw.keys():
            if key in device.keys():
                device[key] = kw[key]

        self.data["data"][end][type].append(device)

    def insert_virtual_printers(self):

        # todo : check
        if self.data["data"]["client"]["printers"] is None:
            self.data["data"]["client"]["printers"] = []
        if self.data["data"]["agent"]["printers"] is None:
            self.data["data"]["agent"]["printers"] = []

        self.data["data"]["client"]["printers"].extend(virtual_printer_client)
        self.data["data"]["agent"]["printers"].extend(virtual_printer_agent)



    def dump(self, tips=''):
        file_name = 'mocked_' + tips
        with open('./mocked/' + file_name + '.json', "w") as f:
            json.dump(self.data, f)




# todo:test
if __name__ == '__main__':
    case = '1u10u'

    mock = Mock()
    mock.generate_device('USB', 'client',is_id_fixed= True, hasProblem = True)


    mock.generate_device('USB','agent',isRebootNeeded = True, isPresent = False)


    mock.insert_virtual_printers()
    mock.info()
    mock.dump(case)

    url = 'http://127.0.0.1:5000/protocols/data_collector'
    #url = 'http://10.117.43.99:8088/api/protocols/data_collector'
    r = requests.post(url, json=json.dumps(mock.data))
    print(r.text)
