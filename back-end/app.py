from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/matrix', methods=['GET'])
def hello_world():
    item = Matrix.query.all()
    item = list(map(lambda x: x.to_json(), item))
    demo = 'from sever'
    return {
        'code': 20022,
        'data': demo
    }


if __name__ == '__main__':
    app.run(debug = True) # 不可用于生产环境