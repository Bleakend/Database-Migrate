import os
import sys
import logging
import pandas as pd
import pyodbc
import yaml
from Column import Column

#Helper functions
def parse_config_yaml():
    try:
        file = open(YAML_CONFIG_FILE, "r")
        yaml_config = yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Error faced when trying to read Yaml file: {e}")
        sys.exit()

    for item in yaml_config.values():
        if(len(item.strip()) == 0):
            logging.error("One or more config parameters are Empty!! Please check the config file.")
            sys.exit()

    server_name = yaml_config["Server name"]
    database_name = yaml_config["Database name"]
    input_directory = yaml_config["Input directory"]

    return server_name, database_name, input_directory
        

def is_valid_extention(file_name: str) -> bool:
    file_path = DIRECTORY_PATH + file_name

    if(not os.path.isfile(file_path)):
        return False

    if(not file_name.endswith(".txt")):
        return False
    
    return True

def is_empty_directory(input_files: list) -> bool:
    input_files_length = len(input_files)
    if(input_files_length):
        logging.info(f"there are {input_files_length} .txt files available in the directory")
        return False
    
    logging.warning("the directory has no files with the extention .txt! Please make sure The files are in the correct directory")
    return True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d,%H:%M:%S',
)

#CONSTANTS
YAML_CONFIG_FILE = r"config.yaml"
SERVER_NAME, DATABASE_NAME, DIRECTORY_PATH = parse_config_yaml()


connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                            f"Server={SERVER_NAME};"
                            f"Database={DATABASE_NAME};"
                            "Trusted_Connection=yes;")

# cursor = connection.cursor()
# cursor.execute("drop table test")
# connection.commit()
# connection.close()
## Main starting point
# input_files = os.listdir(DIRECTORYPATH)
# input_files = list(filter(is_valid_extention, input_files))
# is_empty_directory(input_files)


d = {'a': 1, 'b': 2, 'c': 3.0}
series = pd.Series(data=d, index=['a', 'b', 'c'], name="test")
column = Column(series)