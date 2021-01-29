### flask L10n

> workflow

1. ```powershell
   pip install flask-babel
   ```

2. Init babel and get locale in app.py 

   ```python
   from flask_babel import Babel
   from flask import request
   
    
   app = Flask(__name__)
   babel = Babel(app)
   @babel.localeselector
   def get_locale():
       language = locale.getdefaultlocale()
       return language
   ```

3. Create babel.cfg 

   ```python
   [python: **.py]#Find all marked text
   extensions=jinja2.ext.autoescape,jinja2.ext.with_
   ```

4. Generate translation file template

   ```python
   pybabel extract -F babel.cfg -o messages.pot .#-F:the config file -o:output
   ```

5. Init .po file

   ```python
   pybabel init -i messages.pot -d translations -l zh#-i:translation template;-d:output .po;-l:translation language
   ```

6. Edit .po file(edit msgstr)

   ```python
   #: flask-ext3.py:31
   msgid "No users"
   msgstr "没有用户"
    
   #: flask-ext3.py:32
   msgid "%(num)d user"
   msgid_plural "%(num)d users"
   msgstr[0] "%(num)d个用户"
    
   #: templates/hello.html:2
   msgid "Test Sample"
   msgstr "测试范例"
    
   #: templates/hello.html:3
   msgid "Hello World!"
   msgstr "世界，你好！"
   ```

7. Compile .po file into .mo file

   ```python
   pybabel compile -d translations
   ```

> Translation file update
>
1.  run the commands

   ```powershell
   ```cd to the back-end\src directory
    $ pybabel extract -F babel.cfg -o messages.pot .
    $ pybabel update -i messages.pot -d translations
    ```
2.  Edit messages.po to update the translations.

3.  run the command
    ```powershell
    $ pybabel compile -d translations
    ```
