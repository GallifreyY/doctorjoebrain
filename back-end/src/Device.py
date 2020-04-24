class Device:
    def __init__(self, index, type, end, vid, pid, name, has_p):
        self.index = index
        self.type = type
        self.end = end
        self.vid = vid
        self.pid = pid
        self.name = name
        self.has_problem = has_p

    def find_details_in(self, collected_data):
        devices = collected_data[self.end][self.type]
        return devices[self.index] if len(devices) >= self.index else None

    def is_usb_redirect(self):
        return self.vid is not None and self.pid is not None

    def find_redirection_in_agent(self,collected_data):
        if self.type != 'printers' or 'printers' not in collected_data['agent'].keys():
            return None

        for printer in collected_data['agent']['printers']:
            if printer['Name'] == self.name + '(vdi)':  # todo:update!!
                return printer
        return None
