# todo：when deploying,please first run this python file...

import Config
Config.SET_ENV('prod')
print(Config.GET_URL())