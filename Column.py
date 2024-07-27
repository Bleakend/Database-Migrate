import pandas as pd

def max_number(a, b):
    if(a >= b):
        return a
    return b

class Column:
    column_name: str
    column_type: str


    def __init__(self, column_pandas: pd.Series):
        self.column_name = column_pandas.name
        self.column_type = column_pandas.dtype#self.convert_datatype(column_pandas)

    def convert_datatype(self, pandas_column: pd.Series):

        pandas_datatype = str(pandas_column.dtype)
        if("int" in pandas_datatype):
            return "int"

        if("float" in pandas_datatype):
            max_decimal_points_pandas = len(pandas_column.astype("str").str.split(".", expand=True)[1].max())
            max_number_pandas = len(pandas_column.astype("str").str.split(".", expand=True)[0].max())
            sql_decimal_points = max_number(2, max_decimal_points_pandas)
            sql_number = max_number(12, max_number_pandas)

            return f"decimal({sql_number}, {sql_decimal_points})"

        if("datetime" in pandas_datatype):
            TIME_REGEX = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

            if(pandas_column.astype("str").str.match(TIME_REGEX).any()):
                return "datetime"
            
            return "date"
        
        if("object" in pandas_datatype):
            max_characters_number = int(pandas_column.str.len().max())
            sql_characters_number = max_number(255, max_characters_number)

            return f"nvarchar({sql_characters_number})"

        #will need to add logic for handling when the datatype is not detected
        return "Unidentified"