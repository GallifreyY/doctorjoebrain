from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from flask import jsonify
from flask import request



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *
from util import *

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


####### api: user
@app.route('/user/login', methods = ['GET','POST'])
@cross_origin()
def log_in():
    print(request.json)
    user_name = request.json['userName']
    password = request.json['password']
    token = 'false'
    roles = []
    if(validate(user_name,password)):
        print("successful login")
        token = 'true'
        roles = validate_roles(user_name)

    return {
        'code': 20022,
        'data':{
            'token': token,
            'name': user_name,
            'roles': roles
        }
    }

@app.route('/user/logout', methods = ['GET','POST'])
@cross_origin()
def log_out():
    return{
        'code': 20022,
        'data': 'successfully log out'
    }


######## api: device_info
@app.route('/device_info', methods=['GET'])
@cross_origin()
def device_info():
    # get_device_id()
    device_id = 0  # demo

    # query from db
    item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(Device.device_id == device_id) \
        .with_entities(Device.device_id, Device.device_name, Device.description,
                       Device.picture, Vendor.vendor_id, Vendor.vendor_name,
                       Vendor.vendor_link, Vendor.vendor_logo).all()
    item = to_json_join(item)
    if(len(item)!= 1):
        return{'code':444}
    item = item[0]

    # be strictly consistent with the front
    device_column_data = [
        {'key': "Device Name", 'value': item['device_name']},
        {'key': "Vendor Name", 'value': item['vendor_name']},
        {'key': "VID", 'value': "vid-"+ str(item['vendor_id'])},
        {'key': "PID", 'value': "pid" + str(item['device_id'])}
    ]
    return{
        'code': 20022,
        'data':{
            'name': item['device_name'],
            'pic': item['picture'],
            'link' :item['vendor_link'] ,
            'logo' : item['vendor_logo'],
            'description': item['description'],
            'data': device_column_data
        }

    }







######## api: client_info







######### api: diagnosis_info






if __name__ == '__main__':
    app.run(debug = True) # 不可用于生产环境