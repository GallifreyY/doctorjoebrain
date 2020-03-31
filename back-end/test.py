from models import *
from util import *
import json
import requests
response = requests.get('http://127.0.0.1:5000/matrix')
res = response.text
res = json.loads(res)
print(res)

# # item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(Device.device_id == 0)\
# #     .with_entities(Device.device_id, Device.device_name,Device.description,
# #                    Device.picture, Vendor.vendor_id,Vendor.vendor_name,
# #                    Vendor.vendor_link, Vendor.vendor_logo).all()
#
# # #a = list(map(lambda x: x.to_json(), item))
# # b = to_json_join(item)
#
#
# # print(b)
#
#
# # device_id = 0
# # device_info = Device.query.filter(Device.device_id == device_id)
# # print(item)
#
# item = Matrix.query.join(Driver, Driver.device_id == Matrix.device_id)\
#     .join(Device,Device.device_id == Matrix.device_id)\
#     .with_entities(Device.device_name,Device.device_version,Device.picture,
#                    Matrix.client_os_name,Matrix.Horizon_client_version,
#                    Matrix.agent_os_name,Matrix.Horizon_agent_version,
#                    Driver.agent_driver,Driver.client_driver).all()
# item = to_json_join(item)
# print(item)