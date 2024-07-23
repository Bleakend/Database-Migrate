import os
import sys
import logging
import pandas as pd
import pyodbc
import yaml
from Table import Table
from sql_generation import *

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
    logging.info(f"Config file has been read successfully!!")

    server_name = yaml_config["Server name"].strip()
    database_name = yaml_config["Database name"].strip()
    input_directory = yaml_config["Input directory"].strip()

    return server_name, database_name, input_directory
        

def is_valid_extention(file_name: str) -> bool:
    file_path = DIRECTORY_PATH +  file_name

    if(not os.path.isfile(file_path)):
        return False

    if(not file_name.endswith(".xlsx")):
        return False
    
    return True

def is_empty_directory(input_files: list) -> bool:
    input_files_length = len(input_files)
    if(input_files_length):
        logging.info(f"there are {input_files_length} .xlsx files available in the directory\n")
        return False
    
    logging.warning("the directory has no files with the extention .xlsx! Please make sure The files are in the correct directory")
    return True

def read_tables(directory, input_files):
    tables = []
    for file in input_files:
        table = Table(pd.read_excel(directory + file))
        tables.append(table)
    return tables


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d,%H:%M:%S',
)

#CONSTANTS
YAML_CONFIG_FILE = r"config.yaml"
SERVER_NAME, DATABASE_NAME, DIRECTORY_PATH = parse_config_yaml()
DIRECTORY_PATH += "/"


# connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
#                             f"Server={SERVER_NAME};"
#                             f"Database={DATABASE_NAME};"
#                             "Trusted_Connection=yes;")

# cursor = connection.cursor()
# cursor.execute("drop table test")
# connection.commit()
# connection.close()
## Main starting point
input_files = os.listdir(DIRECTORY_PATH)
input_files = list(filter(is_valid_extention, input_files))
is_empty_directory(input_files)

tables = read_tables(DIRECTORY_PATH, input_files)
sql = tables[0]
print(generate_create_table_sql_statment(sql.columns))