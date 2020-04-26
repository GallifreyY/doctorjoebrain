import requests
import json

url = 'http://127.0.0.1:5000/protocols/data_collector'
# url = 'http://10.117.43.99:8088/api/protocols/data_collector' # dev

file_name = 'real1'

with open ("./mock/" + file_name + ".json") as f:
    data = json.load(f)
data = json.dumps(data)


r = requests.post(url, json=data)
print(r.text)

