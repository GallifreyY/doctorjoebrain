# -*- coding: UTF-8 -*-

from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from flask import request

app = Flask(__name__)
babel = Babel(app)
app.config.from_object('db_info')
db = SQLAlchemy(app)
language = 'en-US'

from models import *
from util import *
from diagnosis import diagnosis, diagnosis_general_issues
import json
import password_access
import handleDB


@babel.localeselector
def get_locale():
    global language
    if is_language_zh_cn(language):
        language = 'zh_Hans_CN'
    elif is_language_zh_tw(language):
        language = 'zh_Hant_TW'
    else:
        language = 'en_US'
    return language

CATE_MAP = {
    "Other Devices": -1,
    "USB Disks": 0,
    "USB Printers": 1,
    "Scanners": 2,
    "Cameras": 3,
    "USB Speech Mics": 4,
    "Smart Cards": 5,
    "Key Boards": 6,
    "Mouses": 7,
    "Signature Pads": 8,
    "PIN Pads": 9,
    "Credit Cards Reader": 10,
    "Fingerprint Readers": 11,
    "Barcode Scanners": 12,
    "Serial Port Devices": 13,
    "Audio": 14,
    "Foot Pedal": 15,
    "Mouse": 16,
    "Keyboard": 17
}

TRS_CN_CATE_MAP = {
    "其它设备": -1,
    "USB硬盘": 0,
    "USB打印机": 1,
    "扫描仪": 2,
    "摄像头": 3,
    "USB语音麦克风": 4,
    "智能卡": 5,
    "键盘": 6,
    "鼠标": 7,
    "签名板": 8,
    "PIN键盘": 9,
    "信用卡": 10,
    "指纹读取器": 11,
    "条码扫描器": 12,
    "串口设备": 13,
    "音频设备": 14,
    "脚踏板": 15,
    "鼠标": 16,
    "键盘": 17
}
TRS_TW_CATE_MAP = {
    "其他設備": -1,
    "USB磁盤": 0,
    "USB打印機": 1,
    "掃描儀": 2,
    "攝像頭": 3,
    "USB語音麥克風": 4,
    "智能卡": 5,
    "鍵盤": 6,
    "鼠標": 7,
    "簽名板": 8,
    "PIN鍵盤": 9,
    "信用卡": 10,
    "指紋讀取器": 11,
    "條碼掃描器": 12,
    "串口設備": 13,
    "音頻設備": 14,
    "腳踏板": 15,
    "鼠標": 16,
    "鍵盤": 17
}
TYPE_DICT = {
    "usbdisk": {"zh_cn": "USB硬盘", "en": "USB Disks","zh_tw":"USB磁盤"},
    "usbprinters": {"zh_cn": "USB打印机", "en": "USB Printers","zh_tw":"USB打印機"},
    "virtualprinters": {"zh_cn": "虚拟打印机", "en": "Virtual Printers","zh_tw":"虛擬打印機"},
    "scanners": {"zh_cn": "扫描仪", "en": "Scanners","zh_tw":"掃描儀"},
    "cameras": {"zh_cn": "摄像头", "en": "Cameras","zh_tw":"攝像頭"},
    "signaturepad": {"zh_cn": "签名板", "en": "Signature Pads","zh_tw":"簽名板"},
    "audio": {"zh_cn": "USB音箱", "en": "USB Audio","zh_tw":"USB音箱"},
    "speechmic": {"zh_cn": "USB语音麦克风", "en": "USB Speech Mics","zh_tw":"USB語音麥克風"},
    "barcodescanner": {"zh_cn": "USB扫码枪", "en": "Barcode Scanner","zh_tw":"USB掃碼槍"},
    "smartcardreader": {"zh_cn": "智能卡读卡器", "en": "Smartcard Reader","zh_tw":"智能卡讀卡器"},
    "mouse": {"zh_cn": "鼠标", "en": "Mouse","zh_tw":"鼠標"},
    "keyboard": {"zh_cn": "键盘", "en": "Keyboard","zh_tw":"鍵盤"},
    "others": {"zh_cn": "其它设备", "en": "Other Devices","zh_tw":"其他設備"}
}
CATE_LIST = []
TRS_CN_CATE_LIST = []
TRS_TW_CATE_LIST = []
for key in CATE_MAP:
    if CATE_MAP[key] == -1: continue
    CATE_LIST.insert(CATE_MAP[key], key)
for key in TRS_CN_CATE_MAP:
    if TRS_CN_CATE_MAP[key] == -1: continue
    TRS_CN_CATE_LIST.insert(TRS_CN_CATE_MAP[key], key)
for key in TRS_TW_CATE_MAP:
    if TRS_TW_CATE_MAP[key] == -1: continue
    TRS_TW_CATE_LIST.insert(TRS_TW_CATE_MAP[key], key)

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

        collected_json = collected_json.replace("\ufeff", "")
        if util.is_json(collected_json):
            collected_data = json.loads(collected_json)
        else:
            return {
                'state':state,
                'code': code
            }
    else:
        collected_data = json.loads(request.json)

    if collected_data['code'] == code:
        uuid = parse_collected_data(collected_data['data'])
        state = 'success'

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


@app.route('/get_language', methods=['POST'])
@cross_origin()
def get_language():
    global language
    language = request.args.get('data')
    return {
        'code': 20022,
        'language': language
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
        suggestions = diagnosis(collected_data, devices[device_index],language)
        errorType = suggestion_type_judge(suggestions)
        diagnosis_info.append({
            'deviceName': devices[device_index].name,
            'checkResult': check_res,
            'suggestions': suggestions
        })
        diagnosis_type_info.append({
            'deviceEnd': devices[device_index].default_info()['end'],
            'deviceTag': devices[device_index].default_info()['tag'],
            'deviceHasProblem': devices[device_index].default_info()['hasProblem'],
            'deviceDriverName': devices[device_index].default_info()['driverName'],
            'driverVersion': devices[device_index].default_info()['driverVersion'],
            'deviceVendorName': device_vendor_name[device_index],
            'devicePics': devices_pics[device_index],
            'devicePid': devices[device_index].pid,
            'deviceVid': devices[device_index].vid,
            'errorType': errorType,
            'deviceType': devices[device_index].type,
            'deviceName': devices[device_index].name,
            'suggestionInfo': suggestions['suggestion'],
            'errorInfo': suggestions['error'],
            'warningInfo': suggestions['warning'],
            'infoLen': {'errorLen': len(suggestions['error']), 'warningLen': len(suggestions['warning']),
                        'suggestionLen': len(suggestions['suggestion'])}
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

    for item in del_dup_diagnosis_type_info:
        trs_dict = TYPE_DICT.get(item['deviceType'],None)
        if trs_dict==None:
            pass
        else:
            if is_language_zh_cn(language):
                item['deviceType']=TYPE_DICT[item['deviceType']]['zh_cn']
            elif is_language_zh_tw(language):
                item['deviceType']=TYPE_DICT[item['deviceType']]['zh_tw']
            else:
                item['deviceType'] = TYPE_DICT[item['deviceType']]['en']
    # Check the general issues from the collected_data
    general_issues_info = []
    general_issues_info = diagnosis_general_issues(collected_data)
    general_issues_info_error_type = suggestion_type_judge(general_issues_info)

    del_dup_diagnosis_type_info.insert(0,{
        'errorInfo': general_issues_info['error'],
        'warningInfo': general_issues_info['warning'],
        'suggestionInfo': general_issues_info['suggestion'],
        'deviceName': 'General issue',
        'errorType': general_issues_info_error_type,
        'infoLen': {'errorLen': len(general_issues_info['error']), 'warningLen': len(general_issues_info['warning']),
                    'suggestionLen': 0}
    })
    return {
        'code': 20022,
        'data': {
            'basicInfo': basic_info,
            'diagnosisInfo': diagnosis_info,
            'diagnosisTypeInfo': del_dup_diagnosis_type_info,
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
    if is_language_zh_cn(language):
        return {
            'code': 20022,
            'data': matrix,
            'cateList': TRS_CN_CATE_LIST
        }
    elif is_language_zh_tw(language):
        return {
            'code': 20022,
            'data': matrix,
            'cateList': TRS_TW_CATE_LIST
        }
    return {
        'code': 20022,
        'data': matrix,
        'cateList': CATE_LIST
    }


@app.route('/matrix/categoryInfo', methods=['GET'])
@cross_origin()
def get_category_info():
    if is_language_zh_cn(language):
        return {
            'code': 20022,
            'data': TRS_CN_CATE_LIST
        }
    elif is_language_zh_tw(language):
        return {
            'code': 20022,
            'data': TRS_TW_CATE_LIST
        }
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
    if request.json["Horizon_client_version"] != "":
        edit_item.Horizon_client_version, edit_item.Horizon_agent_version = request.json["Horizon_client_version"], \
                                                                            request.json["Horizon_agent_version"]
    if request.json["category"] != "":
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
