import sys
import os
sys.path.insert(0,os.getcwd()+'/src')
# src path always in back-end..

from app import app
app.run(debug = True)
# 不可用于生产环境