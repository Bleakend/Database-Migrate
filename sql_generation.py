from jinja2 import Environment, FileSystemLoader
from Column import Column
import pandas as pd

TEMPLATE_PATH = r"jinja-templates"
CREATE_TABLE_TEMPLATE = r"create table.jinja"
env = Environment(loader = FileSystemLoader(TEMPLATE_PATH))

d = {'a': 1, 'b': 2, 'c': 3.0}
series = pd.Series(data=d, index=['a', 'b', 'c'], name="test")
column = Column(series)
column1 = Column(series)


def generate_create_table_sql_statment():
    template = env.get_template(CREATE_TABLE_TEMPLATE)
    sql_statment = template.render()

    return sql_statment