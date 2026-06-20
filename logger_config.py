import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "C:\\Users\\likevin\\OneDrive - Hewlett Packard Enterprise\\Zerto Product\\script and API\\Webhook2.0\\log"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s")
log_file = os.path.join(LOG_DIR, "zerto-automation.log")

file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

logger = logging.getLogger("ZertoEngine")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)