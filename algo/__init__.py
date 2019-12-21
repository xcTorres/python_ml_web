# @Time    : 20/12/19 16:54
# @Author  :  xcTorres
# @FileName: __init__.py.py

import os
import logging.config
from config import CONFIG_ROOT

logging.config.fileConfig(os.path.join(CONFIG_ROOT, "logging.conf"))
logger = logging.getLogger("algo")


