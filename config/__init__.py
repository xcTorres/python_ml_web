# @Time    : 20/12/19 16:28
# @Author  :  xcTorres
# @FileName: __init__.py.py

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
CONFIG_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_PATH = os.path.join(PROJECT_ROOT, 'web_app')
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')
