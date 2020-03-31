# DoctorJoe Intelligence

## front-end
Solution ： Vue.js + IView UI + Webpack

### Start
``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

###  api design
later..

## back-end

### temporary design
![avatar](./doc_assets/djflow.png)

![avatar](./doc_assets/db-demo.png)

Solution(temp): Flask + sql(mysql?)

### Data interface
collector:
```c
#include <curl/curl.h>
#include <json/json.h>
...
 curl = curl_easy_init();
  /* initalize custom header list (stating that Expect: 100-continue is not
     wanted */ 
  headerlist = curl_slist_append(headerlist, buf);
  if(curl) {
    /* what URL that receives this POST */ 
    curl_easy_setopt(curl, CURLOPT_URL, "http://10.117.43.99/api/protocol/upload_device_info");
    if ( (argc == 2) && (!strcmp(argv[1], "noexpectheader")) )
      /* only disable 100-continue header if explicitly requested */ 
      curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headerlist);
    curl_easy_setopt(curl, CURLOPT_HTTPPOST, formpost);

```
+ https://curl.haxx.se/libcurl/c/libcurl-tutorial.html
+ https://blog.csdn.net/qq_32619837/article/details/89155787?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task


web service：
directly get json:
```python
import json
import requests
response = requests.get('http://127.0.0.1:5000/matrix')
res = response.text
res = json.loads(res)
```

set a new api
```python 
@app.route('/protocol/upload_device_info, methods=['GET','POST'])
@cross_origin()
def protocols():
    ...
```

define code:
```json
{
    code:20022, //此处是否还需要添加一个用户的识别码？
    device_info:{
        device_name: "xxx",
        ....
    },
    client_info:{
        ...
    },
    agent_info:{
        ...
    }
}

```
process logic：

```py
def process_device(device_info):
    get_device_from_json()
    if device not in db.device:
        add device into db
    return device_name

def process_matrix(client_info, agent_info)
    get_matrix_from_json()
    if (client,agent,..) in  db.matrix:
        add_suggestions("...")

def diagnosis():
    ...
    return suggestions
```

   