import uuid
import sys
import pickle
from Device import Device as _Device

sys.path.append('../data/user/')
import os
import datetime
import json
import password_access
from collections import OrderedDict


def to_json(inst, cls):
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return d


def to_json_join(items):
    return [dict(zip(item.keys(), item)) for item in items]


def validate(user_name, password):
    flag = password_access.password_deposit("admin",password)
    print(flag)
    if flag:
        return True
    return False


def validate_roles(user_name):
    return ['admin']


def parse_collected_data(data):
    uuid = _generate_uuid()

    save_data(data, uuid, 'user', 'json')
    return uuid


def _generate_uuid():
    return str(uuid.uuid4())


def recognize_devices(collected_data, uuid):
    """
    :param collected_data:
    :return: devices(on duplicated item)
    """
    res = []
    recorded_devices = ['usbdisk', 'virtualprinters','usbprinters', 'scanners', 'cameras','others','signaturepad', 'speechmic','audio']
    for end in collected_data.keys():  # agent or client
        for key in collected_data[end].keys():
            # todo: dimiss pritners check at agent end
            #if key == 'printers' and end == 'agent':
                #continue

            if collected_data[end][key] is None:
                continue
            if key in recorded_devices:
                device_type = key
                devices = collected_data[end][device_type]
                if devices is None:
                    continue

                # todo：detect device key and parse to list
                if isinstance(devices, dict):
                    devices = [devices]
                    collected_data[end][device_type] = devices
                    save_data(collected_data, uuid, 'user', 'json')

                if device_type == 'virtualprinters' or device_type == 'usbprinters':
                    for key in collected_data[end][device_type]:
                        for k, v in dict.items(key):
                            if k == 'DriverName':
                                for index, device in enumerate(devices):
                                    res.append(_Device(index,
                                                device_type,
                                                end,
                                                uuid,
                                                device.get("VID", None),
                                                device.get("PID", None),
                                                device.get('Name', None),
                                                device.get('hasProblem', None),
                                                device.get('problemCode',None),
                                                device.get('problemdesc',None),
                                                device.get('isRebootNeeded', None),
                                                device.get('isPresent', None),
                                                device.get('WorkOffline', None),
                                                v.get('Name', None),
                                                v.get('DriverVersion', None)))

                else:
                    for index, device in enumerate(devices):
                                res.append(_Device(index,
                                            device_type,
                                            end,
                                            uuid,
                                            device.get("VID", None),
                                            device.get("PID", None),
                                            device.get('Name', None),
                                            device.get('hasProblem', None),
                                            device.get('problemCode',None),
                                            device.get('problemdesc',None),
                                            device.get('isRebootNeeded', None),
                                            device.get('isPresent', None),
                                            device.get('WorkOffline', None),
                                            device.get('driverprovider', None),
                                            device.get('driverver', None)))

    return res


def save_data(data, file_name, dir='user', mode='json'):
    today = str(datetime.date.today())
    root_dir = os.path.abspath('..')
    path = os.path.join(root_dir, "prod", "data",dir,today)
    #path = './data/' + dir + '/' + today + '/'
    if not os.path.exists(path):
        print(os.getcwd())
        os.makedirs(path)

    file_mode = 'wb' if mode == 'pickle' else 'w'
    with open(path+'/'+file_name+'.'+mode, file_mode) as f:
        if mode == 'pickle':
            pickle.dump(data, f)
        elif mode == 'json':
            f.write(json.dumps(data))
        else:
            pass


def read_data(file_name, dir='user', mode='json'):
    root_dir = os.path.abspath('..')
    path = os.path.join(root_dir, "prod", "data", dir)
    file_mode = 'rb' if mode == 'pickle' else 'r'
    for list_dir in os.listdir(path):
        dir_path = os.path.join(path, list_dir)
        for file in os.listdir(dir_path):
            if str(file) == file_name + '.' + mode:
                with open(os.path.join(dir_path, file), file_mode) as f:
                    if mode == 'pickle':
                        data = pickle.load(f)
                    elif mode == 'json':
                        data = json.load(f)
                    else:
                        data = None
                return data


def add_info_to_db(collected_data):
    """
    just add the info to db
    :return: None
    """
    return None


##########################################
### todo: Analyze the collected data
##########################################

def get_client_info(collected_data):
    if collected_data['client'] is None:
        return None

    return [
        {'key': "Client OS", 'value': collected_data['client']['OSname'] + ' ' + collected_data['client']['OSver']},
        {'key': "Horizon Version(Client)", 'value': collected_data['client']['clientver']}
    ]


def get_agent_info(collected_data):
    if collected_data['agent'] is None:
        return None
    if collected_data['agent']['OSver'] is None:
        print("null")
        collected_data['agent']['OSver']=" "
    return [
        {'key': "Agent OS", 'value': collected_data['agent']['OSname'] + ' ' + collected_data['agent']['OSver']},
        {'key': "Horizon Version(Agent)", 'value': collected_data['agent']['agentver']}
    ]


def get_client_details_from_agent(collected_data):
    if collected_data['agent'] is None:
        return None
    details = collected_data['agent'].get('clientDetails', None)
    if details is not None:
        return [{'key': "IP Address", 'value': details.get('IP_Address', 'null')},
                {'key': "Broker DNS Name", 'value': details.get('Broker_DNS_Name', 'null')},
                {'key': "Broker User Name", 'value': details.get('Broker_UserName', 'null')},
                {'key': "Broker ID", 'value': details.get('Broker_Farm_ID', 'null')},
                {'key': "Broker IP Address", 'value': details.get('Broker_Gateway_IP_Address', 'null')},
                {'key': "Broker_GatewayHost", 'value': details.get('Broker_GatewayHost', 'null')},
                {'key': "Broker_DomainName", 'value': details.get('Broker_DomainName', 'null')},
                {'key': "Broker_GatewayLocation", 'value': details.get('Broker_GatewayLocation', 'null')},
                {'key': "Broker_GatewayType", 'value': details.get('Broker_GatewayType', 'null')},
                {'key': "Broker_Remote_IP_Address", 'value': details.get('Broker_Remote_IP_Address', 'null')},
                {'key': "Broker_Request_Path", 'value': details.get('Broker_Request_Path', 'null')},
                {'key': "Broker_Tunneled", 'value': details.get('Broker_Tunneled', 'null')},
                {'key': "Broker_URL", 'value': details.get('Broker_URL', 'null')},
                {'key': "Client_ID", 'value': details.get('Client_ID', 'null')},
                {'key': "Client_Version", 'value': details.get('Client_Version', 'null')},
                {'key': "Device_UUID", 'value': details.get('Device_UUID', 'null')},
                {'key': "Displays.Number", 'value': details.get('Displays.Number', 'null')},
                {'key': "Displays.SystemDpi", 'value': details.get('Displays.SystemDpi', 'null')},
                {'key': "Displays.Topology", 'value': details.get('Displays.Topology', 'null')},
                {'key': "Displays.TopologyV2", 'value': details.get('Displays.TopologyV2', 'null')},
                {'key': "Keyboard.KeyDelayToRepeat", 'value': details.get('Keyboard.KeyDelayToRepeat', 'null')},
                {'key': "Keyboard.KeyRepeatRate", 'value': details.get('Keyboard.KeyRepeatRate', 'null')},
                {'key': "Keyboard.Language", 'value': details.get('Keyboard.Language', 'null')},
                {'key': "Keyboard.Layout", 'value': details.get('Keyboard.Layout', 'null')},
                {'key': "Keyboard.NumFuncKeys", 'value': details.get('Keyboard.NumFuncKeys', 'null')},
                {'key': "Keyboard.NumIndicators", 'value': details.get('Keyboard.NumIndicators', 'null')},
                {'key': "Keyboard.NumKeys", 'value': details.get('Keyboard.NumKeys', 'null')},
                {'key': "Keyboard.ScanCodeMode", 'value': details.get('Keyboard.ScanCodeMode', 'null')},
                {'key': "Keyboard.SubType", 'value': details.get('Keyboard.SubType', 'null')},
                {'key': "Keyboard.Type", 'value': details.get('Keyboard.Type', 'null')},
                {'key': "Language", 'value': details.get('Language', 'null')},
                {'key': "Launch_ID", 'value': details.get('Launch_ID', 'null')},
                {'key': "Launch_SessionType", 'value': details.get('Launch_SessionType', 'null')},
                {'key': "LoggedOn_Domainname", 'value': details.get('LoggedOn_Domainname', 'null')},
                {'key': "LoggedOn_FQDN", 'value': details.get('LoggedOn_FQDN', 'null')},
                {'key': "LoggedOn_Username", 'value': details.get('LoggedOn_Username', 'null')},
                {'key': "MAC_Address", 'value': details.get('MAC_Address', 'null')},
                {'key': "Machine_Domain", 'value': details.get('Machine_Domain', 'null')},
                {'key': "Machine_FQDN", 'value': details.get('Machine_FQDN', 'null')},
                {'key': "Machine_Name", 'value': details.get('Machine_Name', 'null')},
                {'key': "Mouse.Identifier", 'value': details.get('Mouse.Identifier', 'null')},
                {'key': "Mouse.NumButtons", 'value': details.get('Mouse.NumButtons', 'null')},
                {'key': "Protocol", 'value': details.get('Protocol', 'null')},
                {'key': "Type", 'value': details.get('Type', 'null')},
                {'key': "TZID", 'value': details.get('TZID', 'null')},
                {'key': "Windows_Timezone", 'value': details.get('Windows_Timezone', 'null')},
                ]

    return None


def check_compatibility(collected_data, device):
    dict_list = {'USBArbitrator':collected_data['client'].get('USBArbitrator', 'N/A'),\
                 'audioService':collected_data['client'].get('audioService', 'N/A'), \
                 'clientPrint':collected_data['client'].get('PrinterService', 'N/A'), \
                 'agentPrint':collected_data['agent'].get('PrinterService', 'N/A'), \
                 'scannerClientService':collected_data['client'].get('scannerClientService','N/A'),\
                 'netlinkClientService':collected_data['client'].get('netlinkClientService', 'N/A'),\
                 'agentAudioService':collected_data['agent'].get('audioService', 'N/A'),\
                 'scannerAgentService':collected_data['agent'].get('scannerAgentService', 'N/A'),\
                 'netlinkAgentService':collected_data['agent'].get('netlinkAgentService', 'N/A'),\
                 'CDRService':collected_data['agent'].get('CDRservice', 'N/A'),\
                 'netlinkSessionService':collected_data['agent'].get('netlinkSessionService', 'N/A')}
    for key,value in dict_list.items():
        if value=="null" or value=="" or value==None:
           dict_list[key] = 'N/A'
    client = [
        {'key': "Client OS Name", 'value': collected_data['client']['OSname'], 'check': True},
        {
            'key': "Client OS Version",
            'value': collected_data['client']['OSver'],
            'check': True
        },

        {'key': "Horizon Version", 'value': collected_data['client']['clientver'], 'check': True},
        {
            'key': "Print Spooler Service",
            'value': dict_list['clientPrint'],
            'check': collected_data['client'].get('PrinterService', None) == 'Running'
        }, {
            'key': "USB Arbitrator Service",
            'value': dict_list['USBArbitrator'],
            'check': collected_data['client'].get('USBArbitrator', None) == 'Running'
        }, {
            'key': "Windows Audio Service",
            'value': dict_list['audioService'],
            'check': collected_data['client'].get('audioService', None) == 'Running'
        }, {
            'key': "VMware Scanner Redirection Client service",
            'value':  dict_list['scannerClientService'],
            'check': collected_data['client'].get('scannerClientService', None) == 'Running'
        },{
            'key': "VMware Netlink Supervisor service",
            'value': dict_list['netlinkClientService'],
            'check': collected_data['client'].get('netlinkClientService', None) == 'Running'
        }, {
            'key': "",
            'value': None,
            'check': 'null'
        }
    ]

    agent = [
        {'key': "Agent OS Name", 'value': collected_data['agent']['OSname'], 'check': True},
        {
            'key': "Agent OS Version",
            'value': collected_data['agent']['OSver'],
            'check': True
        },
        {'key': "Horizon Version", 'value': collected_data['agent']['agentver'], 'check': True},
        {
            'key': "Print Spooler Service",
            'value': dict_list['agentPrint'],
            'check': collected_data['agent'].get('PrinterService', None) == 'Running'
        },
        {
            'key': "CDR Service",
            'value': dict_list['CDRService'],
            'check': collected_data['agent'].get('CDRservice', None) == 'Running'
        },
        {
        'key': "Windows Audio Service",
        'value': dict_list['agentAudioService'],
        'check': collected_data['agent'].get('audioService', None) == 'Running'
        },
        {
            'key': "VMware Scanner Redirection Agent service",
            'value': dict_list['scannerAgentService'],
            'check': collected_data['agent'].get('scannerAgentService', None) == 'Running'
        },
        {
            'key': "VMware Netlink Supervisor service",
            'value': dict_list['netlinkAgentService'],
            'check': collected_data['agent'].get('netlinkAgentService', None) == 'Running'
        },
        {
            'key': "VMware Network Session service",
            'value': dict_list['netlinkSessionService'],
            'check': collected_data['agent'].get('netlinkSessionService', None) == 'Running'
        }
    ]

    # todo: for different device, show custom results

    res = {
        'client': client,
        'agent': agent,
    }
    return res