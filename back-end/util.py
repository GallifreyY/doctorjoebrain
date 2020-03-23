def to_json(inst, cls):
    d = dict()
    '''
    获取表里面的列并存到字典里面
    '''
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return d

def validate(user_name, password):
    if(user_name == 'admin' and password == 'ca$hc0w'): # 暂时
        return True
    return False

def validate_roles(user_name):
    return ['admin']