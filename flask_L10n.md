### DoctorJoe 编译流程

目录
├─zh-CN
|   ├─LC_MESSAGES
|   |      ├─resource.mo
|   |      └resource.po
├─en-US
|   ├─LC_MESSAGES
|   |      ├─resource.mo
|   |      └resource.po

1. 引入python中Tools/l18n/msgfmt.py文件
2. 编辑resource.po

```python
msgid "hello"
msgstr "你好"
```

3. 生成对应二进制翻译文件*.mo

```po
python msgfmt.py -o zh-CN/LC_MESSAGES/resource.mo zh-CN/LC_MESSAGES/resource.po

```

4. 在py文件对应翻译字符串中引入

```python
import os, gettext
_ = None
def getUserLanguage():
    return "zh-CN"   #正确做法应该从前端传入对应语言环境

# Get loc string by language
def getLocStrings():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    return gettext.translation('resource', currentDir, [getUserLanguage(), "en-US"]).gettext

_ = getLocStrings()
```

5. 在对应翻译的string中直接加入对应的msgid

```py
print(_("Hello"))
```