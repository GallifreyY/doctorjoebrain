# -*- coding: utf-8 -*-
import os,base64
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)  # 64 bits

    if isinstance(password, str):
        password = password.encode("UTF-8")

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


if __name__ == '__main__':
    hashed = encrypt_password('_gggghshshshshsszhangmingyuparanoid1998_8')
    #x=str(hashed, encoding='utf-8')
    #print(x)
    print(type(hashed))
    print(len(hashed))
    print(str(hashed))
    print(len(str(hashed)))
    print(len(str(base64.b64encode(hashed))))
    print(base64.b64decode(base64.b64encode(hashed)))
    print(validate_password(hashed, 'ca$hc0w'))
