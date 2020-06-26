from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from flask_cors import cross_origin
from flask import request

app = Flask(__name__)
app.config.from_object('db_info')
db = SQLAlchemy(app)

from models import *
from util import *
from diagnosis import diagnosis
import json
import re
import copy
import configparser

# todo: read data from config file
cf = configparser.ConfigParser()
cf.read("./config.ini")
cf.get('PROD','HTTPS_AD')
ENV = cf.get('ENV','ENV')

if ENV == 'PROD':
    URL = 'https://'+ cf.get('PROD','HTTPS_AD') + ':' + cf.get('PROD','PORT') + '/#/diagnosis/'
else:
    URL = 'http://'+ cf.get('DEV','LOCAL') + ':'+cf.get('DEV','PORT') + '/#/diagnosis/'

print(ENV,URL)

CATE_MAP = {
    "Other Devices" : -1,
    "USB Disks": 0,
    "Printers": 1,
    "Scanners" : 2,
    "Cameras" : 3,
    "USB Speech Mics" : 4,
    "Smart Cards":5,
    "Key Boards" : 6,
    "Mouses" : 7,
    "Signature Pads" : 8,
    "PIN Pads" : 9,
    "Credit Cards" : 10,
    "Fingerprint Readers": 11,
    "Barcode Scanners" :12,
    "Serial Port Devices" :13
}

CATE_LIST = []
for key in CATE_MAP:
    if CATE_MAP[key] == -1: continue
    CATE_LIST.insert(CATE_MAP[key],key)


@app.route('/test',methods=['GET'])
@cross_origin()
def test():
    return 'Hello!'

# protocols to collector
@app.route('/protocols/data_collector', methods=['GET', 'POST'])
@cross_origin()
def add_to_log_file():
    code = 20022
    state = 'failed'
    url = ''


    if not request.is_json:
        # Fixme: please update a more strong method to pare String data from collector
        form = request.form.to_dict()
        for item in form.items():
            collected_json = ''
            for json_section in item:
                json_section = json_section.replace("\n", "").replace("\'", "\"")
                collected_json += json_section
        collected_data = json.loads(collected_json)
    else:
        collected_data = json.loads(request.json)

    if collected_data['code'] == code:
        uuid = parse_collected_data(collected_data['data'])
        state = 'success'
        url = URL + uuid

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
    for index, device in enumerate(devices):

        device_info = device.default_info()

        # query vendor
        if device.vid is not None:
            item = Vendor.query.filter(Vendor.vendor_id == device.vid).with_entities(Vendor.vendor_name,
                                                                                     Vendor.vendor_link,
                                                                                     Vendor.vendor_logo).all()
            if len(item) == 1:
                item = item[0]
                device_info['details']['vendor_name'], \
                device_info['details']['vendor_link'], \
                device_info['details']['vendor_logo'] = item

        # todo: query device
        if not (device.vid is None or device.pid is None):
            # device_id = device.vid + '-' + device.pid
            item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(
                and_(Device.vendor_id== device.vid, Device.product_id== device.pid)) \
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
        'agent': agent_column_data,
        'clientDetail': client_detail_data
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



###########api：matrix
@app.route('/matrix', methods=['GET'])
@cross_origin()
def matrix():
    # query from db
    matrix = Matrix.query.join(Device,
                               and_(and_(Device.product_id == Matrix.product_id, Device.vendor_id == Matrix.vendor_id),
                                    or_(Matrix.model == None, Matrix.model == Device.model)
                                    )
                               ).with_entities(Device.device_name, Device.category,
                                               Matrix.product_id, Matrix.vendor_id, Matrix.model,
                                               Matrix.Horizon_client_version, Matrix.Horizon_agent_version,
                                               ).all()

    matrix = to_json_join(matrix)
    return {
        'code': 20022,
        'data': matrix,
        'cateList': CATE_LIST
    }


@app.route('/matrix/categoryInfo', methods=['GET'])
@cross_origin()
def get_category_info():
    return {
        'code': 20022,
        'data': CATE_LIST
    }



# reminder delete:
# >>> db.session.delete(me)
# >>> db.session.commit()

@app.route('/matrix/newData', methods=['GET', 'POST'])
@cross_origin()
def matrix_new_data():
    print(request.json)
    res = request.json

    # todo: extract device info
    new_device = {'vendor_id': res['vid'], 'product_id': res['pid'], 'device_name': res['deviceName'],
                  "category": CATE_MAP.get(res["category"],-1),
                  "model": None if res["model"] is None or len(res["model"]) == 0 else res["model"]}
    query_res = Device.query.filter(
        and_(Device.vendor_id == res["vid"], Device.product_id == res["pid"], Device.model == new_device["model"] )).all()

    if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid'])!=0  :
        insert_item = Device(**new_device)
        db.session.add(insert_item)
        db.session.commit()
        print("Inserted to the DB - Device table : {}".format(new_device))

    # todo: spread items for Matrix DB
    for versions in res["HorizonVersionsRes"]:
        if len(versions['client']) == 0 or len(versions['agent']) == 0:
            continue
        new_matrix = {'vendor_id': res['vid'], 'product_id': res['pid'],
                      "model": None if res["model"] is None or len(res["model"]) == 0 else res["model"],
                      "Horizon_client_version" : versions['client'],
                      "Horizon_agent_version": versions['agent'],
                      }
        query_res = Matrix.query.filter_by(**new_matrix).all()
        if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid'])!=0:
            insert_item = Matrix(**new_matrix)
            db.session.add(insert_item)
            db.session.commit()
            print("Inserted to the DB - Matrix table : {}".format(new_matrix))


    # todo:spread items for driver DB
    for os in res["OS"]:
        if len(os) == 0: continue
        new_driver = {'vendor_id': res['vid'], 'product_id': res['pid'],
                      "model": None if res["model"] is None or len(res["model"]) == 0 else res["model"],
                      "driver": res['driver'],
                      "os_name": os
                      }
        query_res = Driver.query.filter_by(**new_driver).all()
        if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid'])!=0:
            insert_item = Driver(**new_driver)
            db.session.add(insert_item)
            db.session.commit()
            print("Inserted to the DB - Driver table : {}".format(new_driver))


    return {
        'code': 20022,
        'data': 'success'
    }

@app.route('/matrix/deletedData', methods=['GET', 'POST'])
@cross_origin()
def matrix_delete_data():
    Matrix.query.filter_by(**request.json).delete()
    db.session.commit()
    return {
        'code': 20022,
        'data': 'success'
    }

@app.route('/matrix/editedData', methods=['GET','POST'])
@cross_origin()
def matrix_edit_data():
    # print(request.json)
    edit_item = Matrix.query.filter_by(**request.json['query']).first()
    edit_item.Horizon_client_version, edit_item.Horizon_agent_version = request.json["Horizon_client_version"], request.json["Horizon_agent_version"]
    db.session.commit()

    return {
        'code': 20022,
        'data': 'success'
    }





if __name__ == 'main':

    app.run(debug=(ENV == 'DEV'))
