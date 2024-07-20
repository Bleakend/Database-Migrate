import pandas as pd

class Column:
    column_name: str
    column_type: str


    def __init__(self, column_pandas: pd.Series):
        self.column_name = column_pandas.name
        self.column_type = column_pandas.dtypes