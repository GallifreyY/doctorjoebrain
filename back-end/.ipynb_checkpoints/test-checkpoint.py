from src.models import *
from src.util import *

item = Device.query.join(Vendor, Vendor.vendor_id == Device.vendor_id).filter(Device.device_id == 0)\
    .with_entities(Device.device_id, Device.device_name,Device.description,
                   Device.picture, Vendor.vendor_id,Vendor.vendor_name,
                   Vendor.vendor_link, Vendor.vendor_logo).all()

#a = list(map(lambda x: x.to_json(), item))
b = to_json_join(item)


print(b)


# device_id = 0
# device_info = Device.query.filter(Device.device_id == device_id)
# print(item)