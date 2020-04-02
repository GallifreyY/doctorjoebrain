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


####### protocal to collector
app.route('/protocols/data_collector', methods = ['GET','POST'])
@cross_origin()
def add_to_log_file():
    if(request.json['code'] != 20022):
        return{'code':444}






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
    # uuid = request.json['uuid'] #识别用户
    # get_device_id(uuid)
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
@app.route('/client_info', methods=['GET'])
@cross_origin()
def client_info():
    # get_client_info()
    client_info = {
        'data':[
            {'key': "Client OS", 'value': "Windows 10 64bits 1903"},
            {'key': "Client Hardware", 'value': "Dell Optiplex 7060"}
        ]
    }

    return{
        'code': 20022,
        'data': client_info
    }


######### api: diagnosis_info
@app.route('/diagnosis_info', methods=['GET'])
@cross_origin()
def diagnosis_info():
    # diagnosis()
    # return suggestions & videos
    suggestions = [
      "PowerMic is a USB composite device. It is recommended to use Nuance extension solution to redirect this device instead of USB redirection.",
      "Please follow the guide of Nuance to configure the extensions on client and agent side.",
      "If you don’t use the extension solution, you can follow the KB to configure the GPO for USB split on Horizon agent machine."
    ]
    video = "PowerMic.mp4"

    # client & agent check
    # 可以此处再加个函数做格式转换
    client =  [
      { 'key': "Client OS", 'value': "Windows 10 64bits 1903", 'check': True },
      {
        'key': "Client Hardware",
        'value': "Dell Optiplex 7060",
        'check': True
      },
      { 'key': "PowerMic Firmware", 'value': "1.4.1", 'check': True },
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
      { 'key': "Horizon client version", 'value': "5.2", 'check': True },
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
    agent  =[
      { 'key': "Agent OS", 'value': "Windows 10 64bits 1903", 'check': False },
      { 'key': "Agent Hardware", 'value': "vSphere VM", 'check': False },
      { 'key': "PowerMic Firmware", 'value': "1.41", 'check': False },
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
      { 'key': "Horizon agent version", 'value': "7.10", 'check': True },
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

    return{
        'code':20022,
        'data':{
            'client':client,
            'agent':agent,
            'suggestions': suggestions,
            'referenceVideo' : video
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
    matrix= to_json_join(matrix)
    return {
        'code':20022,
        'data': matrix
    }





if __name__ == '__main__':
    app.run(debug = True) # 不可用于生产环境