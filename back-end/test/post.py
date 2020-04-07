import requests
import json

url = 'http://127.0.0.1:5000/protocols/data_collector'  # 本地
data = json.dumps({
    'code': 20022,
    'data': {
        'client': {
            "OSname": "Windows 10",
            "OSver": "1909",
            "clientver": "8.0.0.11085",
            "usbdisk": {
                "VID": "090C",
                "PID": "1000",
                "manufacturer": "Compatible USB storage device",
                "name": "USB Mass Storage Device",
                "driverprovider": "Microsoft",
                "driverver": "10.0.18362.1",
                "isRebootNeeded": False,
                "isPresent": True,
                "hasProblem": False

            }
        },
        'agent': {
            "OSname": "Windows 10",
            "OSver": "1909",
            "agentver": "7.12.0",
            "Horizoncomp": {
                "VmVideo": 1,
                "VmwVdisplay": 1,
                "VmwVidd": 1,
                "ScannerRedirection": 1,
                "SerialPortRedirection": 1,
                "SmartCard": 1,
                "TSMMR": 1,
                "ThinPrint": 1,
                "USB": 1,
                "V4V": 1,
                "VPA": 1,
                "VmwVaudio": 1,
                "DeviceBridgeBAS": 1,
                "SdoSensor": 1,
                "HelpDesk": 1,
                "RDP": 1,
                "BlastUDP": 1,
                "Core": 1,
                "VMWMediaProviderProxy": 1,
                "ClientDriveRedirection": 1,
                "RTAV": 1,
                "FLASHMMR": 1,
                "GEOREDIR": 1,
                "PerfTracker": 1,
                "SVIAgent": 0,
                "NGVC": 0,
                "PrintRedir": 0
            },
            "usbdisk": {
                "VID": "090C",
                "PID": "1000",
                "manufacturer": "Compatible USB storage device",
                "name": "USB Mass Storage Device",
                "driverprovider": "Microsoft",
                "driverver": "10.0.18362.1",
                "isRebootNeeded": False,
                "isPresent": True,
                "hasProblem": False
            },
            "CDRservice": "Running"
        }

    }
})
r = requests.post(url, json=data)
print(r.text)
