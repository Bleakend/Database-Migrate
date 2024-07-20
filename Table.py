import pandas as pd

class Table:
    pandas_dataframe: pd.DataFrame
    primary_key: str
    columns: list

    def __init__(self, dataframe):
        self.pandas_dataframe = dataframe