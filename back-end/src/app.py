from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from flask import request

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *
from util import *
from diagnosis import diagnosis
import json


####### just for testing..
# @app.route('/matrix', methods=['GET'])
# def hello_world():
#     item = Matrix.query.all()
#     item = list(map(lambda x: x.to_json(), item))
#     demo = 'from sever'
#     return {
#         'code': 20022,
#         'data': demo
#     }


# protocols to collector
@app.route('/protocols/data_collector', methods=['GET', 'POST'])
@cross_origin()
def add_to_log_file():
    # print(request.json)
    code = 20022
    state = 'failed'
    url = ''
    collected_data = json.loads(request.json)
    if collected_data['code'] == code:
        uuid = parse_collected_data(collected_data['data'])
        state = 'success'
        # dev vm:
        url = 'http://10.117.43.99:8088/api/diagnosis/' + uuid
        # local:
        url = 'http://127.0.0.1:8080/#/diagnosis/' + uuid

    return {'code': code,
            'state': state,
            'url': url
            }


####### api: user
@app.route('/user/login', methods=['GET', 'POST'])
@cross_origin()
def log_in():
    user_name = request.json['userName']
    password = request.json['password']
    token = 'false'
    roles = []
    if (validate(user_name, password)):
        print("successful login")
        token = 'true'
        roles = validate_roles(user_name)

    return {
        'code': 20022,
        'data': {
            'token': token,
            'name': user_name,
            'roles': roles
        }
    }


@app.route('/user/logout', methods=['GET', 'POST'])
@cross_origin()
def log_out():
    return {
        'code': 20022,
        'data': 'successfully log out'
    }


#
######## api: device_info
@app.route('/device_and_client_info', methods=['GET'])
@cross_origin()
def device_and_client_info():
    uuid = request.args.get('id')
    collected_data = read_data(uuid, 'user', 'json')
    if collected_data == None:
        return {'code': 20044}
    devices = recognize_devices(collected_data)
    save_data(devices, uuid, 'devices', 'pickle')
    # todo: directly get info from collected_data
    client_info = get_client_info(collected_data)
    # todo: add info to devices
    add_info_to_db(collected_data)

    devices_info = []
    # todo walk all devices
    for index,device in enumerate(devices):
        device_info = {
            "index": index,
            "device_name": device.name,
            "vid": device.vid,
            "pid": device.pid
        }

        # todo: query
        device_id = device.vid + '-' + device.pid  # demo
        item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(Device.device_id == device_id) \
            .with_entities(Device.description,
                           Device.picture, Vendor.vendor_name,
                           Vendor.vendor_link, Vendor.vendor_logo).all()

        item = to_json_join(item)

        if len(item) == 1:
            item = item[0]
            device_info["details"] = item

        # if query multiple or no data in db - no detail info

        devices_info.append(device_info)
    print(devices_info)

    client_column_data = [
        {'key': "Client OS", 'value': client_info['client_os']},
        {'key': "Horizon Version(Client)", 'value': client_info['Horizon_version_client']}
    ]
    return {
        'code': 20022,
        'data': {
            'device': devices_info,
            'client': {
                'client_column_data': client_column_data
            }
        }

    }


######### api: diagnosis_info
@app.route('/diagnosis_info', methods=['GET'])
@cross_origin()
def diagnosis_info():
    uuid = request.args.get('id')
    collected_data = read_data(uuid, 'user', 'json')
    if collected_data is None:
        return {'code': 20044}
    # todo：直接读取保证顺序
    devices = read_data(uuid,'devices','pickle')
    # todo :find index
    device = devices[0]
    # todo: compatibility check
    # check_compatibility (collected_data)
    # todo: diagnosis
    suggestions = diagnosis(collected_data, device)

    # fake data
    client = [
        {'key': "Client OS", 'value': "Windows 10 64bits 1903", 'check': True},
        {
            'key': "Client Hardware",
            'value': "Dell Optiplex 7060",
            'check': True
        },
        {'key': "PowerMic Firmware", 'value': "1.4.1", 'check': True},
        {
            'key': "Setting",
            'value': "USB split GPO setting in Client side",
            'check': False
        },
        {
            'key': "Setting",
            'value': "USB split registy setting in Client side",
            'check': False
        },
        {'key': "Horizon client version", 'value': "5.2", 'check': True},
        {
            'key': "Horizon client USB arbitrator Service status",
            'value': "Running",
            'check': True
        },
        {
            'key': "Horizon client log level",
            'value': "Information",
            'check': True
        },
        {
            'key': "Nuance solution",
            'value': "Nuance PowerMic VMware Client Extension",
            'check': False
        }
    ]
    agent = [
        {'key': "Agent OS", 'value': "Windows 10 64bits 1903", 'check': False},
        {'key': "Agent Hardware", 'value': "vSphere VM", 'check': False},
        {'key': "PowerMic Firmware", 'value': "1.41", 'check': False},
        {
            'key': "Setting",
            'value': "USB split GPO setting in agent side",
            'check': False
        },
        {
            'key': "Setting",
            'value': "USB split registy setting in agent side",
            'check': False
        },
        {'key': "Horizon agent version", 'value': "7.10", 'check': True},
        {
            'key': "Horizon agent USB arbitrator Service status",
            'value': "Runing",
            'check': True
        },
        {
            'key': "Horizon agent log level",
            'value': "Information",
            'check': True
        },
        {
            'key': "Nuance solution",
            'value': "Nuance PowerMic VMware Agent Extension",
            'check': False
        }
    ]
    video = "PowerMic.mp4"

    return {
        'code': 20022,
        'data': {
            'client': client,
            'agent': agent,
            'suggestions': suggestions,
            'referenceVideo': video
        }
    }


###########api：matrix
@app.route('/matrix', methods=['GET'])
@cross_origin()
def matrix():
    # query from db
    matrix = Matrix.query.join(Driver, Driver.device_id == Matrix.device_id) \
        .join(Device, Device.device_id == Matrix.device_id) \
        .with_entities(Device.device_name, Device.device_version, Device.picture,
                       Matrix.client_os_name, Matrix.Horizon_client_version,
                       Matrix.agent_os_name, Matrix.Horizon_agent_version,
                       Driver.agent_driver, Driver.client_driver).all()

    matrix = to_json_join(matrix)
    return {
        'code': 20022,
        'data': matrix
    }
