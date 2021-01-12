# -*- coding: UTF-8 -*-
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
from diagnosis import diagnosis, diagnosis_general_issues
import json
import re
import copy
import configparser
import password_access
import handleDB


CATE_MAP = {
    "Other Devices": -1,
    "USB Disks": 0,
    "Virtual Printers": 1,
    "USB Printers": 2,
    "Scanners": 3,
    "Cameras": 4,
    "USB Speech Mics": 5,
    "Smart Cards": 6,
    "Key Boards": 7,
    "Mouses": 8,
    "Signature Pads": 9,
    "PIN Pads": 10,
    "Credit Cards": 11,
    "Fingerprint Readers": 12,
    "Barcode Scanners": 13,
    "Serial Port Devices": 14
}

CATE_LIST = []
for key in CATE_MAP:
    if CATE_MAP[key] == -1: continue
    CATE_LIST.insert(CATE_MAP[key], key)


@app.route('/test', methods=['GET'])
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
        # url = URL + uuid

    return {'code': code,
            'state': state,
            'uuid': uuid
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
    devices_pics = []
    device_vendor_name = []
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
                and_(Device.vendor_id == device.vid, Device.product_id == device.pid)) \
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
        devices_pics.append(device_info['details']['picture'])
        device_vendor_name.append(device_info['details']['vendor_name'])
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
    diagnosis_type_info = []
    for device_index in range(len(devices)):
        check_res = check_compatibility(collected_data, devices[device_index])
        suggestions = diagnosis(collected_data, devices[device_index])
        if(len(suggestions['error'])>0) and (len(suggestions['warning'])==0) and (len(suggestions['suggestion'])==0):
            errorType = 1
        elif (len(suggestions['error'])==0) and (len(suggestions['warning'])>0) and (len(suggestions['suggestion'])==0):
            errorType = 0
        elif (len(suggestions['error'])>0) and (len(suggestions['warning'])>0) and (len(suggestions['suggestion'])==0):
            errorType = 2
        elif (len(suggestions['error'])>0) and (len(suggestions['warning'])==0) and (len(suggestions['suggestion'])>0):
            errorType = 11
        elif (len(suggestions['error'])>0) and (len(suggestions['warning'])>0) and (len(suggestions['suggestion'])>0):
            errorType = 21
        elif (len(suggestions['error'])==0) and (len(suggestions['warning'])>0) and (len(suggestions['suggestion'])>0):
            errorType = 10
        else:
            errorType =-1
        diagnosis_info.append({
            'deviceName':devices[device_index].name,
            'checkResult': check_res,
            'suggestions': suggestions
        })
        diagnosis_type_info.append({
            'deviceEnd': devices[device_index].default_info()['end'],
            'deviceTag':devices[device_index].default_info()['tag'],
            # 'deviceIp': devices[device_index].default_info().is_present,
            # 'deviceIur': devices[device_index].default_info().is_usb_redirect,
            # 'deviceIvp': devices[device_index].default_info().is_virtual_printer,
            'deviceHasProblem': devices[device_index].default_info()['hasProblem'],
            'deviceDriverName':devices[device_index].default_info()['driverName'],
            'driverVersion':devices[device_index].default_info()['driverVersion'],
            'deviceVendorName': device_vendor_name[device_index],
            'devicePics':devices_pics[device_index],
            'devicePid': devices[device_index].pid,
            'deviceVid': devices[device_index].vid,
            'errorType':errorType,
            'deviceType': devices[device_index].type,
            'deviceName': devices[device_index].name,
            'suggestionInfo': suggestions['suggestion'],
            'errorInfo':suggestions['error'],
            'warningInfo':suggestions['warning'],
            'infoLen':{'errorLen':len(suggestions['error']),'warningLen':len(suggestions['warning']),'suggestionLen':len(suggestions['suggestion'])}
        })


    del_dup_diagnosis_type_info = []
    seen = set()
    for item in diagnosis_type_info:
        if (item['deviceType'] == 'virtualprinters' or item['deviceType'] == 'usbprinters'):
            if item['deviceName'] not in seen:
                seen.add(item['deviceName'])
                del_dup_diagnosis_type_info.append(item)
        else:
            del_dup_diagnosis_type_info.append(item)
    
    # Check the general issues from the collected_data
    general_issues_info = []
    general_issues_info = diagnosis_general_issues(collected_data)


    return {
        'code': 20022,
        'data': {
            'basicInfo': basic_info,
            'diagnosisInfo': diagnosis_info,
            'diagnosisTypeInfo':del_dup_diagnosis_type_info,
            'generalIssueInfo': general_issues_info
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
                  "category": CATE_MAP.get(res["category"], -1),
                  "model": None if res["model"] is None or len(res["model"]) == 0 else res["model"]}
    query_res = Device.query.filter(
        and_(Device.vendor_id == res["vid"], Device.product_id == res["pid"],
             Device.model == new_device["model"])).all()

    if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid']) != 0:
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
                      "Horizon_client_version": versions['client'],
                      "Horizon_agent_version": versions['agent'],
                      }
        query_res = Matrix.query.filter_by(**new_matrix).all()
        if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid']) != 0:
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
        if len(query_res) == 0 and len(res['vid']) != 0 and len(res['pid']) != 0:
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


@app.route('/matrix/editedData', methods=['GET', 'POST'])
@cross_origin()
def matrix_edit_data():
    print(request.json)
    edit_item = Matrix.query.filter_by(**request.json['query']).first()
    db.session.query(Device).filter(Device.product_id == request.json["query"]["product_id"],
                                    Device.vendor_id == request.json["query"]["vendor_id"],
                                    Device.model == request.json["query"]["model"]).update(
        {'device_name': request.json["edit"]["device_name"]})
    if request.json["Horizon_client_version"]!="":
        edit_item.Horizon_client_version, edit_item.Horizon_agent_version = request.json["Horizon_client_version"], \
                                                                        request.json["Horizon_agent_version"]
    if request.json["category"]!="":
        db.session.query(Device).filter(Device.product_id == request.json["query"]["product_id"],
                                        Device.vendor_id == request.json["query"]["vendor_id"],
                                        Device.model == request.json["query"]["model"]).update(
            {'category': CATE_MAP.get(request.json["category"], -1)})
    # device_item.device_name = request.json["edit"]["device_name"]
    # device_item.category = CATE_MAP.get(request.json["edit"]["category"], -1)

    db.session.commit()

    return {
        'code': 20022,
        'data': 'success'
    }


@app.route('/reg', methods=['GET', 'POST'])
@cross_origin()
def password_modify():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        password = post_data.get('password')
        oldpasswd = post_data.get('oldpasswd')
        sql_search = "SELECT password FROM user WHERE username = '%s';" % ('admin')
        count, result, conn = handleDB.find_mysql(sql_search)
        if count == 0:
            password_access.insert_password("admin", password)
            message = 1
        else:
            flag = password_access.password_deposit("admin", oldpasswd)
            if flag:
                repeat = password_access.password_deposit("admin", password)
                if repeat:
                    message = 2
                else:
                    password_access.modify_password(password)
                    message = 1
            else:
                message = 0
    else:
        response_object['message'] = 'none!'
    return {
        'code': 20022,
        'data': message
    }


@app.route('/result', methods=['GET'])
@cross_origin()
def trs_result():
    response_object = {'status': 'success'}
    sql_search = "SELECT password FROM user WHERE username = '%s';" % ('admin')
    count, result, conn = handleDB.find_mysql(sql_search)
    if count == 1:
        flag = password_access.password_deposit("admin", "changeme")
        if flag:
            count = 0
    response_object['message'] = count
    conn.close()
    return {
        'code': 20022,
        'data': response_object
    }


if __name__ == '__main__':
    app.run(debug=(ENV == 'DEV'))
