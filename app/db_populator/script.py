import os
from app.db_populator.parsers.json_parser import JSONFileParser

parser = JSONFileParser()
working_dir = os.getcwd()
data_dir = f"{working_dir}/app/db_populator/data/"


def get_beverage_data() -> dict:
    beverage_data = parser.parse(f"{data_dir}/beverages.json")
    return beverage_data


def get_ingredient_data() -> dict:
    ingredient_data = parser.parse(f"{data_dir}/ingredients.json")
    return ingredient_data


def get_size_data() -> dict:
    size_data = parser.parse(f"{data_dir}/sizes.json")
    return size_data


def get_customer_data() -> dict:
    customer_data = parser.parse(f"{data_dir}/customers.json")
    return customer_data

