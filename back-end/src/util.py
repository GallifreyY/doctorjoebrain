import uuid
import sys
import pickle

sys.path.append('../data/user/')  # 进入user文件夹
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
    """
    :param items: 联表查询的结果
    :return: 字典
    """
    return [dict(zip(item.keys(), item)) for item in items]


def validate(user_name, password):
    if (user_name == 'admin' and password == 'ca$hc0w'):  # 暂时
        return True
    return False


def validate_roles(user_name):
    return ['admin']


class _Device:
    def __init__(self, type, end, vid, pid, name, has_p):
        self.type = type
        self.end = end  # agent or client
        self.vid = vid
        self.pid = pid
        self.name = name
        self.has_problem = has_p


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
    :bug: 无序的读取 -- 目前选择将device数据存起来 保证书序
    """
    devices = []
    recorded_devices = ['usbdisk']
    for end in collected_data.keys():  # agent or client
        for key in collected_data[end].keys():
            if key in recorded_devices:
                device_type = key
                for device in collected_data[end][device_type]:
                    devices.append(_Device(device_type,
                                           end,
                                           device["VID"],
                                           device["PID"],
                                           device['name'],
                                           device['hasProblem']))

    # todo: 存取device信息避免二次计算
    return devices


def save_data(data, file_name, dir='user', mode='json'):
    """
    :param dir: 目录
    :param file_name:
    :param data:
    :return:
    # todo: 存数据 避免二次计算
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
    }


def check_compatibility(collected_data,device):
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
