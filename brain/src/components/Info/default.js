const df = {
  deviceInfo: {
    name: "mock product",
    pic: "mic.jpg",
    link: "mock link",
    logo: "nuance.jpg",
    description: "mock description",
    data: [
      { key: "Device Name", value: "mock product" },
      { key: "Vendor Name", value: "vendor.." },
      { key: "VID", value: "vid-x" },
      { key: "PID", value: "pid-x" }
    ]
  },
  clientInfo: {
    data: [
      { key: "Client OS", value: "Windows 10 64bits 1903" },
      { key: "Client Hardware", value: "Dell Optiplex 7060" }
    ]
  },
  compatilityCheck: {
    columns: [
      { title: "Key", key: "key" },
      { title: "Value", key: "value" },
      {
        title: "Check",
        key: "check",
        width: 100,
        render: (h, params) => {
          let _string = "Pass";
          let _color = "success";
          console.log(params);
          if (params.row.check == false) {
            _string = "Failed";
            _color = "error";
          }
          return h(
            "Tag",
            {
              props: { color: _color, size: "small", type: "border" }
            },
            _string
          );
        }
      }
    ],
    client: [
      { key: "Client OS", value: "Windows 10 64bits 1903", check: true },
      {
        key: "Client Hardware",
        value: "Dell Optiplex 7060",
        check: true
      },
      { key: "PowerMic Firmware", value: "1.4.1", check: true },
      {
        key: "Setting",
        value: "USB split GPO setting in Client side",
        check: false
      },
      {
        key: "Setting",
        value: "USB split registy setting in Client side",
        check: false
      },
      { key: "Horizon client version", value: "5.2", check: true },
      {
        key: "Horizon client USB arbitrator Service status",
        value: "Runing",
        check: true
      },
      {
        key: "Horizon client log level",
        value: "Information",
        check: true
      },
      {
        key: "Nuance solution",
        value: "Nuance PowerMic VMware Client Extension",
        check: false
      }
    ],
    agent: [
      { key: "Agent OS", value: "Windows 10 64bits 1903", check: false },
      { key: "Agent Hardware", value: "vSphere VM", check: false },
      { key: "PowerMic Firmware", value: "1.41", check: false },
      {
        key: "Setting",
        value: "USB split GPO setting in agent side",
        check: false
      },
      {
        key: "Setting",
        value: "USB split registy setting in agent side",
        check: false
      },
      { key: "Horizon agent version", value: "7.10", check: true },
      {
        key: "Horizon agent USB arbitrator Service status",
        value: "Runing",
        check: true
      },
      {
        key: "Horizon agent log level",
        value: "Information",
        check: true
      },
      {
        key: "Nuance solution",
        value: "Nuance PowerMic VMware Agent Extension",
        check: false
      }
    ],
    suggestions: [
      "PowerMic is a USB composite device. It is recommended to use Nuance extension solution to redirect this device instead of USB redirection.",
      "Please follow the guide of Nuance to configure the extensions on client and agent side.",
      "If you don’t use the extension solution, you can follow the KB to configure the GPO for USB split on Horizon agent machine."
    ],
    referenceVedio: "PowerMic.mp4"
  }

}
module.exports = df


