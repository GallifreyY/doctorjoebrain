import sys
import os
sys.path.insert(0,os.getcwd()+'/src')

import json
from app import app

app.run(debug = False)
