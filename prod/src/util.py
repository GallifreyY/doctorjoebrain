import uuid
import sys

sys.path.append('../data/user/')  # 进入user文件夹
import os
import datetime
import json


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


def parse_collected_data(data):
    uuid = _generate_uuid()
    today = str(datetime.date.today())
    path = '../data/user/' + today + '/'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + uuid + '.json', "w") as f:
        f.write(json.dumps(data))

    return uuid


def _generate_uuid():
    return str(uuid.uuid4())


def locate_json(uuid):
    """
    :return: info(type:dict)
    """
    path = '../data/user/'
    for dir in os.listdir(path):
        if os.path.isfile(dir):
            continue
        dir_path = os.path.join(path, dir)

        for file in os.listdir(dir_path):
            if str(file) == uuid + '.json':
                with open(os.path.join(dir_path, file), "r") as f:
                    data = json.load(f)
                return data


def recognize_devices(collected_data):
    """

    :param collected_data:
    :return: devices(on duplicated item)
    """
    devices = []
    recorded_devices = ['usbdisk']
    for end in collected_data.values():  # agent or client
        for key in end.keys():
            if key in recorded_devices:
                devices.append(key)

    return list(set(devices))


def recognize_end(collected_data, device):
    '''
    不考虑“都存在”的情况
    :param device:
    :param collected_data:
    :return:
    '''
    if device in collected_data['client'].keys():
        return 'client'
    else:
        return 'agent'


def add_info_to_db(collected_data):
    """
    just add the info to db
    :return: None
    """
    return None


def get_static_info(collected_data, device):
    """
    :param collected_data, device: just for one device
    :return: dict including device id/name vendor id/name:
    """
    end = recognize_end(collected_data, device)
    return {
        'device_name': collected_data[end][device]['name'],
        'pid': collected_data[end][device]['PID'],
        'vid': collected_data[end][device]['VID'],
        'client_os': collected_data['client']['OSname'] + ' ' + collected_data['client']['OSver'],
        'Horizon_version_client': collected_data['client']['clientver'],
    }
