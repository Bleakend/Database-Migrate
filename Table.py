import pandas as pd
from Column import Column
from logging_config import *
config_logging()

class Table:
    primary_key: str
    columns: list

    def __init__(self, dataframe: pd.DataFrame):
        self.columns = []
        for column_name in dataframe.columns:
            column = dataframe[column_name]
            self.columns.append(Column(column))
        logging.info(f"columns have been read successfully!")