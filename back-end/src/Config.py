class Config:
    SERVER = 'http://10.117.43.99:8088/#/diagnosis/'
    LOCAL = "http://127.0.0.1:8080/#/diagnosis/"
    ENV = 'dev' # dev or prod

def SET_ENV(env):
    if env != 'dev' and  env !='prod':
        env = 'dev'
        print('the env name only can be dev or prod')

    Config.ENV = env

def info():
    return Config

def GET_URL():
    if Config.ENV == 'dev':
        return Config.LOCAL
    elif Config.ENV == 'prod':
        return Config.SERVER
    else:
        return None
