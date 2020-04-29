# import Config
# print(Config.info().ENV)
# Config.SET_ENV('prod')
# print(Config.GET_URL())
#
import os
print(os.getcwd())
print(str(os.getcwd())[-3:])

import Config
Config.info()