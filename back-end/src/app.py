from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_
from flask_cors import cross_origin
from flask import request

app = Flask(__name__)
app.config.from_object('db_info')
db = SQLAlchemy(app)

from models import *
from util import *
from diagnosis import diagnosis
import json
import Config
import re
import copy


# protocols to collector
@app.route('/protocols/data_collector', methods=['GET', 'POST'])
@cross_origin()
def add_to_log_file():
    code = 20022
    state = 'failed'
    url = ''

    if not request.is_json:
        form = request.form.to_dict()
        for item in form.items():
            collected_json = item[0].replace("\n", "").replace("\'", "\"")
            collected_data = json.loads(collected_json)
    else:
        collected_data = json.loads(request.json)

    if collected_data['code'] == code:
        uuid = parse_collected_data(collected_data['data'])
        state = 'success'
        url = Config.GET_URL() + uuid

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
    devices = recognize_devices(collected_data, uuid)

    # save_data(devices, uuid, 'devices', 'pickle')

    # todo: add info to devices
    add_info_to_db(collected_data)

    devices_info = []
    # todo walk all devices
    for index, device in enumerate(devices):

        device_info = device.default_info()

        # todo: query vendor
        if device.vid is not None:
            item = Vendor.query.filter(Vendor.vendor_id == device.vid).with_entities(Vendor.vendor_name,
                               Vendor.vendor_link, Vendor.vendor_logo).all()
            if len(item) == 1:
                item = item[0]
                device_info['details']['vendor_name'],\
                device_info['details']['vendor_link'],\
                device_info['details']['vendor_logo'] = item

        # todo: query device
        if not (device.vid is None or device.pid is None):
            # device_id = device.vid + '-' + device.pid
            item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(and_(Device.vendor_id == device.vid, Device.product_id == device.pid)) \
                .with_entities(Device.device_name,
                               Device.description,
                               Device.picture, Vendor.vendor_name,
                               Vendor.vendor_link, Vendor.vendor_logo).all()

            item = to_json_join(item)

            if len(item) > 1:
                print("warning: id-query has multiple results")
            elif len(item) == 0:
                print("tips: database are not recorded the device: {}".format(device.vid + "_" + device.pid))
            else:
                item = item[0]
                # todo: if value is None, fill with default
                for key in item.keys():
                    if item[key] is None or len(item[key]) == 0:
                        continue
                    if key in device_info['details'].keys():
                        device_info['details'][key] = item[key]
                    device_info['deviceName'] = item['device_name']

        devices_info.append(device_info)

    # todo: directly get info from collected_data
    client_column_data = get_client_info(collected_data)
    agent_column_data = get_agent_info(collected_data)
    client_detail_data = get_client_details_from_agent(collected_data)

    basic_info = {
        'device': devices_info,
        'client': client_column_data,
        'agent':agent_column_data,
        'clientDetail' : client_detail_data
    }

    diagnosis_info = []
    for device in devices:
        check_res = check_compatibility(collected_data, device)
        suggestions = diagnosis(collected_data, device)
        video = "PowerMic.mp4"

        diagnosis_info.append({
            'checkResult': check_res,
            'suggestions': suggestions,
            'referenceVideo': video
        })

    return {
        'code': 20022,
        'data': {
            'basicInfo': basic_info,
            'diagnosisInfo': diagnosis_info
        }

    }


######### api: diagnosis_info(deprecated)
# @app.route('/diagnosis_info', methods=['GET'])
# @cross_origin()
# def diagnosis_info():
#     uuid = request.args.get('id')
#     index = int(request.args.get('index'))
#     collected_data = read_data(uuid, 'user', 'json')
#     if collected_data is None:
#         return {'code': 20022, 'data': {}}
#     devices = read_data(uuid, 'devices', 'pickle')
#     # todo :find index
#     device = devices[index]
#     # todo: compatibility check
#     check_res = check_compatibility(collected_data, device)
#     # todo: diagnosis
#     suggestions = diagnosis(collected_data, device)
#
#     # print(suggestions)
#     # fake data
#
#     video = "PowerMic.mp4"
#
#     return {
#         'code': 20022,
#         'data': {
#             'checkResult': check_res,
#             'suggestions': suggestions,
#             'referenceVideo': video
#         }
#     }


###########api：matrix
# todo : need to update
@app.route('/matrix', methods=['GET'])
@cross_origin()
def matrix():
    # query from db
    matrix = Matrix.query.join(Device,
                               and_(and_(Device.product_id == Matrix.product_id, Device.vendor_id == Matrix.vendor_id),
                                    or_(Matrix.model == None, Matrix.model == Device.model)
                                   )
                               ).with_entities(Device.device_name,Device.category,
                                               Matrix.product_id, Matrix.vendor_id, Matrix.model,
                                               Matrix.Horizon_client_version,Matrix.Horizon_agent_version,
                                               Matrix.redirect_method).all()

    matrix = to_json_join(matrix)
    return {
        'code': 20022,
        'data': matrix
    }


if __name__ == 'main':
    env = Config.info().ENV
    debug = True if env == 'dev' else False
    app.run(debug=debug)
