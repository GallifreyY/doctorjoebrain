import re
import util
import models
# usbdisk printers
class Device:
    def __init__(self, index, type, end, uuid, vid, pid, name, has_p, irn, is_present):
        self.index = index
        self.type = type
        self.end = end
        self.uuid = uuid
        self.vid = vid
        self.pid = pid
        self.name = name
        self.has_problem = has_p
        self.is_reboot_needed = irn
        self.is_present = is_present

        self.raw_data = self._read_raw_data()
        self.is_usb_redirect = self._is_usb_redirect()

    def _read_raw_data(self):
        return util.read_data(self.uuid)



    def _is_usb_redirect(self):
        # todo:details

        if self.type == 'usbdisk':
            if self.end == 'agent':
                return True
            else:
                return False

        elif self.type == 'printers':
            # printer will be detected only in agent
            if self.vid is not None and self.pid is not None:
                return False

            for device_r in self.raw_data['agent'][self.type]:
                if 'VID' in device_r.keys() and 'PID' in device_r.keys():
                    device_id = device_r['VID'] + '-' + device_r['PID']
                    # todo: query in db
                    item = models.Device.query.filter(models.Device.device_id == device_id).with_entities(
                        models.Device.device_name).one()
                    if len(item) == 1:
                        if item[0] == self.name:
                            self.vid, self.pid = device_r['VID'], device_r['PID']
                            print(item[0])


                            return True

                    # elif device_r.get('vendor') == self.name.replace(" ", ""):
                    #     self.vid, self.pid = device_r['VID'], device_r['PID']
                    #     return True

        return False

    def find_details(self):
        devices = self.raw_data[self.end][self.type]
        return devices[self.index] if len(devices) >= self.index else None

    def is_virtual_printer(self):
        # todo:update
        return self.type == 'printers' and self.vid is None and self.pid is None and not self.is_usb_redirect

    def find_redirection_in_agent(self):
        # just for printers
        # todo:update
        if self.type != 'printers' or 'printers' not in self.raw_data['agent'].keys():
            return None

        for printer_r in self.raw_data['agent']['printers']:
            printer_r_name = printer_r.get('name', None) or printer_r.get('Name', None)
            # todo : future update to re
            if self.name[0:int(len(self.name))] == printer_r_name[0:int(len(self.name))]:
                return printer_r
        return None

    def default_info(self):
        default_info = {
            "deviceName": self.name,
            "vid": self.vid,
            "pid": self.pid,
            "type": self.type,
            "hasProblem":self.has_problem or False,
            "end": self.end,
            "details": {
                'picture': 'devices.jpg',
                'vendor_name': 'unrecorded',
                'vendor_link': 'unrecorded',
                'vendor_logo': 'vendor.png',
                'description': 'This device is not recorded in our database'
            },
            "tag":{
                "isPresent": self.is_present,
                "isRebootNeed": self.is_reboot_needed,
                "isUsbRedirect": self.is_usb_redirect,
                "isVirtualPrinter" : self.is_virtual_printer()
            }
        }
        # todo:
        if self.type == 'usbdisk':
            default_info['details']['picture'] = 'defaultUSB.jpg'
        elif self.type == 'printers':
            default_info['details']['picture'] = 'defaultPrinter.png'

        # todo: just for demo, will add in db in the future
        # if self.type == 'printers' and re.search(r'Brother', self.name):
        #     default_info['picture'] = 'Brother-QL.png'

        # todo: add some photos for virtual printers
        if self.is_virtual_printer():
            default_info['details']['description'] = 'This device is a virtual printer'
            if re.search(r'VMware Global Print', self.name):
                default_info['details']['picture'] = 'VMwareGlobalPrint.png'
            elif re.search(r'Fax', self.name):
                default_info['details']['picture'] = 'Fax.png'
            elif re.search(r'ApeosPort', self.name):
                default_info['details']['picture'] = 'Apeos17F.png'

        return default_info