import os
import random
import string
# path = '../data/user/'
# uuid = "5e2979a2-78de-11ea-a42b-6c4008998958"
# for dir in os.listdir(path):
#     if os.path.isfile(dir):
#         continue
#     dir_path = os.path.join(path, dir)
#
#     for file in os.listdir(dir_path):
#         print(file)

from collections.abc import Iterable

def ranstr(num):
    res = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return res

print(ranstr(6))