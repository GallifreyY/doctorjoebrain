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

####### just for try
@app.route('/matrix', methods=['GET'])
def hello_world():
    item = Matrix.query.all()
    item = list(map(lambda x: x.to_json(), item))
    demo = 'from sever'
    return {
        'code': 20022,
        'data': demo
    }


####### api/user
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






if __name__ == '__main__':
    app.run(debug = True) # 不可用于生产环境