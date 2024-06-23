import yaml
import logging
import json
import os

with open('config/setting.yml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set the desired logging level
info_log = config["log"]["info"]
os.makedirs(os.path.dirname(info_log), exist_ok=True)
file_handler_info = logging.FileHandler(info_log)
formatter_info = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler_info.setFormatter(formatter_info)
logger.addHandler(file_handler_info)

def log_message(message,stdout =False):
    if stdout:
        print(message)
    if not config["log"]["enable_log"]:
        return
    logger.info(message)

def log_error(error_message,stdout =False):
    if stdout:
        print(error_message)
    if not config["log"]["enable_log"]:
        return
    logger.error(error_message)

def update_count_json_file(data):
    if not config["log"]["enable_log"]:
        return
    count_log = config["log"]["count"]
    os.makedirs(os.path.dirname(count_log), exist_ok=True)
    
    with open(count_log, "w+") as file:
        try:
            existing_data = json.load(file)
        except json.JSONDecodeError:
            existing_data = {}
        existing_data.update(data)

        file.seek(0) 
        json.dump(existing_data, file, indent=4)
        file.truncate()

    