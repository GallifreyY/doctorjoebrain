<style scoped>
    .expand-row{
        margin-bottom: 16px;
    }
</style>
<template>
    <div>
        <Row class="rexpand-row">
            <Col span="24" v-if="row.errorType===1">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.errorInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">{{$t("Has problem")}}</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>
  <Col span="24" v-else-if="row.errorType===0">
                <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.warningInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
              <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}} {{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>

          <Col span="24" v-else-if="row.errorType===2">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.errorInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
             <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.warningInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>



             <Col span="24" v-else-if="row.errorType===21">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.errorInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
             <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.warningInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
                <div v-for="(item,i) in row.suggestionInfo">
              <Icon type="ios-alert-outline" color="green" />
              <span class="suggestions">{{row.suggestionInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.suggestionInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.suggestionInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
            </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>

 <Col span="24" v-else-if="row.errorType===11">
                <div v-for="(item,i) in row.errorInfo">
              <Icon type="ios-alert-outline" color="red" />
              <span class="suggestions">{{row.errorInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.errorInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.errorInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
                <div v-for="(item,i) in row.suggestionInfo">
              <Icon type="ios-alert-outline" color="green" />
              <span class="suggestions">{{row.suggestionInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.suggestionInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.suggestionInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
            </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>

           <Col span="24" v-else-if="row.errorType===10">
             <div v-for="(item,i) in row.warningInfo">
              <Icon type="ios-alert-outline" color="#FFA500" />
              <span class="suggestions">{{row.warningInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.warningInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.warningInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
                 </div>
                <div v-for="(item,i) in row.suggestionInfo">
              <Icon type="ios-alert-outline" color="green" />
              <span class="suggestions">{{row.suggestionInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.suggestionInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.suggestionInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
            </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>

         <Col span="24" v-else>
                <div v-for="(item,i) in row.suggestionInfo">
              <Icon type="ios-alert-outline" color="green" />
              <span class="suggestions">{{row.suggestionInfo[i].rcontext}}</span>
              <span class="suggestions" v-if="row.suggestionInfo[i].rhasDetail">
                {{$t("Follow")}}
                <a :href="row.suggestionInfo[i].rdetail">
                  {{$t("this link")}}
                  <Icon type="ios-search" size="16" />
                </a>
                {{$t("to find more guidance.")}}
              </span>
            </div>
               <div style="margin-top: 15px">
                <Row style="background:#eee;padding:20px">
        <Col span="8">
            <Card :bordered="false" style="text-align: center;height:390px">
                <p slot="title">{{row.deviceName}}</p>
                <img class="device-img" :src="'/static/device/'+ row.devicePics" style="margin: 0 auto" />
                <div class="diagtag">
              <span slot="extra" style=" font-weight:400;">
              <Tag
                color="success"
                type="border"
                size="default"
              >{{$t("Detected in ")}}{{row.deviceEnd.replace(/^\S/,s =>s.toUpperCase())}}{{$t(" end")}}</Tag>
              <Tag
                v-if="row.deviceTag.isVirtualPrinter"
                color="warning"
                type="border"
              >{{$t("Virtual Printer")}}</Tag>
              <Tag
                v-else-if="row.deviceTag.isPresent"
                color="success"
                type="border"
              >{{$t("Connected")}}</Tag>
              <Tag v-else color="error" type="border">{{$t("Disconnected")}}</Tag>
              <Tag v-if="row.deviceHasProblem" color="error" type="border" style="width: 196px">Has problem</Tag>
              <Tag
                v-if="row.deviceTag.isRebootNeed"
                color="warning"
                type="border"
              >{{$t("Reboot Need")}}</Tag>
              <Tag
                v-if="row.deviceTag.isUsbRedirect"
                color="warning"
                type="border"
              >{{$t("Usb Redirected")}}</Tag>
            </span>
                  </div>
            </Card>
        </Col>
        <Col span="15" offset="1">
            <Card shadow>
                <p slot="title">{{$t("Device Information")}}</p>
             <ul style="list-style: none;" >
            <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Pid</h3><h4 style="margin-right: 20px">{{ row.devicePid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">Vid</h3><h4 style="margin-right: 20px">{{ row.deviceVid}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Device type")}}</h3><h4 style="margin-right: 20px">{{ row.deviceType}}</h4>
            </li>
                <Divider />
                <li style="display: flex;justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Driver Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceDriverName}}</h4>
            </li>
               <Divider />
               <li style="display: flex;
    justify-content: space-between;height:12px">
                 <h3 style="margin-left: 20px">{{$t("Driver Version")}}</h3><h4 style="margin-right: 20px">{{ row.driverVersion}}</h4>
            </li>
                <Divider />
               <li style="display: flex;
    justify-content: space-between;height:22px">
                 <h3 style="margin-left: 20px">{{$t("Vendor Name")}}</h3><h4 style="margin-right: 20px">{{ row.deviceVendorName}}</h4>
            </li>
        </ul>
            </Card>
        </Col>
    </Row>
              </div>
              </Col>




        </Row>
    </div>
</template>
<script>
    export default {
      name: "ReportTableExpand",
        props: {
            row: Object,
            index: Object
        }
    };
</script>
<style>
  .device-img{
    width: 170px;
    height: 170px;
  }
  .diagtag{
    margin-top: 40px;
  }
</style>
