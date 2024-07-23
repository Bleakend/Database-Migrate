from jinja2 import Environment, FileSystemLoader
from Column import Column
import pandas as pd

TEMPLATE_PATH = r"jinja-templates"
CREATE_TABLE_TEMPLATE = r"create table.jinja"
env = Environment(loader = FileSystemLoader(TEMPLATE_PATH))

def generate_create_table_sql_statment(columns: list):
    template = env.get_template(CREATE_TABLE_TEMPLATE)
    sql_statment = template.render(columns=columns)

    return sql_statment