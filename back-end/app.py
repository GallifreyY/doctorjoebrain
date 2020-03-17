from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello_world():
    item = Matrix.query.all()
    item = map(lambda x: x.to_json(), item)
    return {
        'code':'2000',
        'data': item
    }


if __name__ == '__main__':
    app.run(debug = True) # 不可用于生产环境