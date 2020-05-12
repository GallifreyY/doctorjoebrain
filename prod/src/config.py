class Config:
    SERVER = 'https://djdev2016:8090/#/diagnosis/'
    LOCAL = "http://127.0.0.1:8080/#/diagnosis/"
    ENV = 'dev' # dev or prod

def SET_ENV(env):
    if env != 'dev' and  env !='prod':
        env = 'dev'
        print('the env name only can be dev or prod')

    Config.ENV = env

def info():
    print(Config.ENV)
    print(GET_URL())
    return Config

def GET_URL():
    if Config.ENV == 'dev':
        return Config.LOCAL
    elif Config.ENV == 'prod':
        return Config.SERVER
    else:
        return None
