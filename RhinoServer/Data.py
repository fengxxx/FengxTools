# Data.py
import logging,os


SERVER=None
SERVER_NAME="RhinoServer"
VERSION=1.0
Version=VERSION

CONNECTIONS=[]

LOG_FILE_PATH=SERVER_NAME+".log"
LOG_FILE_WRITE_MODE="r"
if os.path.isfile(LOG_FILE_PATH):
    LOG_FILE_WRITE_MODE="wb"
else:
    LOG_FILE_WRITE_MODE="wb"

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=LOG_FILE_PATH,
                filemode=LOG_FILE_WRITE_MODE)
