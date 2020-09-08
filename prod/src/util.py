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
    recorded_devices = ['usbdisk', 'printers', 'scanners', 'cameras']
    for end in collected_data.keys():  # agent or client
        for key in collected_data[end].keys():
            # todo: dimiss pritners check at agent end
            if key == 'printers' and end == 'agent':
                continue

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

                for index, device in enumerate(devices):
                    res.append(_Device(index,
                                       device_type,
                                       end,
                                       uuid,
                                       device.get("VID", None),
                                       device.get("PID", None),
                                       device.get('name', None) or device.get('Name', None),
                                       device.get('hasProblem', None),
                                       device.get('isRebootNeeded', None),
                                       device.get('isPresent', None)))

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
        return [{'key': "IP Address", 'value': details['IP_Address']},
                {'key': "Broker DNS Name", 'value': details['Broker_DNS_Name']},
                {'key': "Broker User Name", 'value': details['Broker_UserName']},
                {'key': "Broker ID", 'value': details['Broker_Farm_ID']},
                {'key': "Broker IP Address", 'value': details['Broker_Gateway_IP_Address']},
                ]

    return None


def check_compatibility(collected_data, device):
    client = [
        {'key': "Client OS Name", 'value': collected_data['client']['OSname'], 'check': True},
        {
            'key': "Client OS Version",
            'value': collected_data['client']['OSver'],
            'check': True
        },

        {'key': "Horizon Version", 'value': collected_data['client']['clientver'], 'check': True},
        {
            'key': "Printer Service",
            'value': collected_data['client']['PrinterService'],
            'check': collected_data['client'].get('PrinterService', None) == 'Running'
        }, {
            'key': "USB Arbitrator Service",
            'value': collected_data['client'].get('USBArbitrator', None),
            'check': collected_data['client'].get('USBArbitrator', None) == 'Running'
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
            'key': "Printer Service",
            'value': collected_data['agent'].get('PrinterService', None),
            'check': collected_data['agent'].get('PrinterService', None) == 'Running'
        },
        {
            'key': "CDR Service",
            'value': collected_data['agent'].get('CDRservice', None),
            'check': collected_data['agent'].get('CDRservice', None) == 'Running'
        }
    ]

    # todo: for different device, show custom results

    res = {
        'client': client,
        'agent': agent
    }
    return res
