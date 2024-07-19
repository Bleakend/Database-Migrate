import os
import logging

#Constants variables
DIRECTORYPATH = r"Input Files/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%Y-%m-%d,%H:%M:%S',
)

#Helper functions
def is_text_file(file_name: str) -> bool:
    file_path = DIRECTORYPATH + file_name

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

#Main starting point
input_files = os.listdir(DIRECTORYPATH)
input_files = list(filter(is_text_file, input_files))
is_empty_directory(input_files)
