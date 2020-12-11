import re
import util
import models
from sqlalchemy import and_, or_
# usbdisk printers
class Device:
    def __init__(self, index, type, end, uuid, vid, pid, name, has_p, pcode, pdesc, irn, is_present, driverName, driverVersion):
        self.index = index
        self.type = type
        self.end = end
        self.uuid = uuid
        self.vid = vid
        self.pid = pid
        self.name = name
        self.has_problem = has_p
        self.problemcode = pcode
        self.problemdesc = pdesc
        self.is_reboot_needed = irn
        self.is_present = is_present
        self.driverName = driverName
        self.driverVersion = driverVersion

        self.raw_data = self._read_raw_data()
        self.details = self.find_details()
        self.is_usb_redirect = self._is_usb_redirect()
        self.is_virtual_printer = self._is_virtual_printer()
        self.suspected_vendor = self._find_suspected_vendor()
        # self._parse()
        #
        # if self.type == 'printers' and self.find_redirection_in_agent() is not None:
        #     print_r = self.find_redirection_in_agent()
        #     self.vid, self.pid = print_r.get("VID", None), print_r.get("PID", None)
        #     print(print_r)


    #def _parse(self):
        # XXX: parse for some special situation
        # 1. printers: vid& pid were redirected in agent end


    def _read_raw_data(self):
        return util.read_data(self.uuid)

    def _is_usb_redirect(self):
        # todo:details

        if self.type == 'usbdisk' or self.type == 'scanners' or self.type == 'cameras' or self.type == 'others' :
            if self.end == 'agent':
                return True
            else:
                return False

        elif self.type == 'usbprinters' and self.end == 'agent':
            if self.vid is not None and self.pid is not None:
                return True
            else:
                return False
        elif self.type == 'usbprinters' and self.end == 'client':
            if self.vid is not None and self.pid is not None:
                return False

            for device_r in self.raw_data['client'][self.type]:
                if 'VID' in device_r.keys() and 'PID' in device_r.keys():
                    # device_id = device_r['VID'] + '-' + device_r['PID']
                    # todo: query in db
                    item = models.Device.query.filter(and_(models.Device.vendor_id == device_r['VID'],
                                                           models.Device.product_id == device_r['PID']))\
                        .with_entities(models.Device.device_name).all()
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

    def _is_virtual_printer(self):
        # todo:update
        return self.type == 'virtualprinters'

    def find_redirection_in_agent(self):
        # just for printers
        # todo:update
        if self.type != 'virtualprinters' or 'virtualprinters' not in self.raw_data['agent'].keys():
            return None

        for printer_r in self.raw_data['agent']['virtualprinters']:
            printer_r_name = printer_r.get('name', None) or printer_r.get('Name', None)
            # todo : future update to re
            if self.name[0:int(len(self.name))] == printer_r_name[0:int(len(self.name))]:
                return printer_r
        return None

    def _find_suspected_vendor(self):
        if self._is_virtual_printer(): return None
        if self.name == None: return None
        return self.name.split(' ')[0] or None 

    def default_info(self):
        default_info = {
            "deviceName": self.name,
            "vid": self.vid,
            "pid": self.pid,
            "type": self.type,
            "hasProblem":self.has_problem or False,
            "end": self.end,
            "driverName": self.driverName,
            "driverVersion": self.driverVersion,
            "details": {
                'picture': 'devices.jpg',
                'vendor_name':  self.suspected_vendor or 'unrecorded',
                'vendor_link': 'unrecorded',
                'vendor_logo': 'vendor.png',
                'description': 'This device is not recorded in our database'
            },
            "tag":{
                "isPresent": self.is_present,
                "isRebootNeed": self.is_reboot_needed,
                "isUsbRedirect": self.is_usb_redirect,
                "isVirtualPrinter" : self.is_virtual_printer
            }
        }
        # todo:
        if self.type == 'usbdisk':
            default_info['details']['picture'] = 'defaultUSB.jpg'
            default_info['details']['description'] = 'This device is an USB disk'
        elif self.type == 'virtualprinters' or self.type == 'usbprinters':
            default_info['details']['picture'] = 'defaultPrinter.png'
        elif self.type == 'scanners':
            default_info['details']['picture'] = 'defaultScanner.jpg'
            default_info['details']['description'] = 'This device is a scanner'
        elif self.type == 'cameras':
            default_info['details']['picture'] = 'defaultCamera.jpg'
            default_info['details']['description'] = 'This device is a camera'
        elif self.type == 'others':
            default_info['details']['picture'] = 'defaultOther.png'
            default_info['details']['description'] = 'This device is an unknown device.'
            default_info['hasProblem'] = True
        # todo: just for demo, will add in db in the future
        # if self.type == 'printers' and re.search(r'Brother', self.name):
        #     default_info['picture'] = 'Brother-QL.png'

        # todo: add some photos for virtual printers
        if self.is_virtual_printer:
            default_info['details']['description'] = 'This device is a virtual printer'
            if re.search(r'VMware Global Print', self.name):
                default_info['details']['picture'] = 'VMwareGlobalPrint.png'
            elif re.search(r'Fax', self.name):
                default_info['details']['picture'] = 'Fax.png'
            elif re.search(r'ApeosPort', self.name):
                default_info['details']['picture'] = 'Apeos17F.png'

        return default_info