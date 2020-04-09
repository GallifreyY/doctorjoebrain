import os

path = '../data/user/'
uuid = "5e2979a2-78de-11ea-a42b-6c4008998958"
for dir in os.listdir(path):
    if os.path.isfile(dir):
        continue
    dir_path = os.path.join(path, dir)

    for file in os.listdir(dir_path):
        print(file)