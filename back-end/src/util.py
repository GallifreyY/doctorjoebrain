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
    def __init__(self, type, end, vid, pid, name):
        self.type = type
        self.end = end  # agent or client
        self.vid = vid
        self.pid = pid
        self.name = name


def parse_collected_data(data):
    uuid = _generate_uuid()
    # today = str(datetime.date.today())
    # path = '../data/user/' + today + '/'
    # if not os.path.exists(path):
    #     os.mkdir(path)
    # with open(path + uuid + '.json', "w") as f:
    #     f.write(json.dumps(data))
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
    for end in collected_data.values():  # agent or client
        for key in end.keys():
            if key in recorded_devices:
                device_type = key
                for device in end[device_type]:
                    devices.append(_Device(device_type,
                                           end,
                                           device["VID"],
                                           device["PID"],
                                           device['name']))

    # todo: 存取device信息避免二次计算
    return devices


def save_data(data, file_name, dir, mode):
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


def read_data(file_name, dir, mode):
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
