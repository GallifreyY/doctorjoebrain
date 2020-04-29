import sys
import os
sys.path.insert(0,os.getcwd()+'/src')

import json
import Config
from app import app


env = Config.info().ENV
debug = True if env == 'dev' else False


app.run(debug = debug)
