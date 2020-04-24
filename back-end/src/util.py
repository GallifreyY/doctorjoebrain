import uuid
import sys
import pickle
from Device import Device as _Device

sys.path.append('../data/user/')
import os
import datetime
import json
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
    if (user_name == 'admin' and password == 'ca$hc0w'):  # 暂时
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


def recognize_devices(collected_data):
    """
    :param collected_data:
    :return: devices(on duplicated item)
    """
    res = []
    recorded_devices = ['usbdisk', 'printers']
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
                for index, device in enumerate(devices):
                    res.append(_Device(index,
                                       device_type,
                                       end,
                                       device.get("VID", None),
                                       device.get("PID", None),
                                       device.get('name', None) or device.get('Name', None),
                                       device.get('hasProblem', None)))

    return res


def save_data(data, file_name, dir='user', mode='json'):
    """
    :param dir
    :param file_name
    :param data
    :return:
    """
    today = str(datetime.date.today())
    path = '../data/' + dir + '/' + today + '/'
    if not os.path.exists(path):
        os.mkdir(path)
    file_mode = 'wb' if mode == 'pickle' else 'w'
    with open(path + file_name + '.' + mode, file_mode) as f:
        if mode == 'pickle':
            pickle.dump(data, f)
        elif mode == 'json':
            f.write(json.dumps(data))
        else:
            pass


def read_data(file_name, dir='user', mode='json'):
    path = '../data/' + dir + '/'
    file_mode = 'rb' if mode == 'pickle' else 'r'
    for dir in os.listdir(path):
        if os.path.isfile(dir):
            continue
        dir_path = os.path.join(path, dir)

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


def get_client_info(collected_data):
    """
    :param collected_data:
    :return: dict:
    """
    return {
        'client_os': collected_data['client']['OSname'] + ' ' + collected_data['client']['OSver'],
        'Horizon_version_client': collected_data['client']['clientver'],
        'hardware': None
    }


def check_compatibility(collected_data, device):
    client = [
        {'key': "Client OS Name", 'value': collected_data['client']['OSname'], 'check': True},
        {
            'key': "Client OS Version",
            'value': collected_data['client']['OSver'],
            'check': True
        },
        {
            'key': "Client Hardware",
            'value': None,
            'check': False
        },

        {'key': "Horizon Version", 'value': collected_data['client']['clientver'], 'check': True},
        # {
        #     'key': "Setting",
        #     'value': "USB split GPO setting in Client side",
        #     'check': False
        # },
        # {
        #     'key': "Setting",
        #     'value': "USB split registy setting in Client side",
        #     'check': False
        # },
        # {'key': "Horizon client version", 'value': "5.2", 'check': True},
        # {
        #     'key': "Horizon client USB arbitrator Service status",
        #     'value': "Running",
        #     'check': True
        # },
        # {
        #     'key': "Horizon client log level",
        #     'value': "Information",
        #     'check': True
        # },
        # {
        #     'key': "Nuance solution",
        #     'value': "Nuance PowerMic VMware Client Extension",
        #     'check': False
        # }
    ]
    agent = [
        {'key': "Agent OS Name", 'value': collected_data['agent']['OSname'], 'check': True},
        {
            'key': "Agent OS Version",
            'value': collected_data['agent']['OSver'],
            'check': True
        },
        {
            'key': "Agent Hardware",
            'value': None,
            'check': False
        },

        {'key': "Horizon Version", 'value': collected_data['agent']['agentver'], 'check': True}
        # {'key': "PowerMic Firmware", 'value': "1.41", 'check': False},
        # {
        #     'key': "Setting",
        #     'value': "USB split GPO setting in agent side",
        #     'check': False
        # },
        # {
        #     'key': "Setting",
        #     'value': "USB split registy setting in agent side",
        #     'check': False
        # },
        # {'key': "Horizon agent version", 'value': "7.10", 'check': True},
        # {
        #     'key': "Horizon agent USB arbitrator Service status",
        #     'value': "Runing",
        #     'check': True
        # },
        # {
        #     'key': "Horizon agent log level",
        #     'value': "Information",
        #     'check': True
        # },
        # {
        #     'key': "Nuance solution",
        #     'value': "Nuance PowerMic VMware Agent Extension",
        #     'check': False
        # }
    ]
    res = {
        'client': client,
        'agent': agent
    }
    return res
