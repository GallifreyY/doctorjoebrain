# import Config
# print(Config.info().ENV)
# Config.SET_ENV('prod')
# print(Config.GET_URL())
#

# import os
# print(os.getcwd())
# print(str(os.getcwd())[-3:])
#
# import Config
# Config.info()
from util import *
# import models
# device_id = '04F9' + '-' + '2044'
# it = models.Device.query.filter(models.Device.device_id == device_id).with_entities(models.Device.device_name).one()
# print(it[0])

import configparser
cf = configparser.ConfigParser()
cf.read("../config.ini")
print(cf.get('ENV','ENV'))
print(type(cf.get('ENV','ENV')))