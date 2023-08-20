import os
from app.db_populator.parsers import FileParser


def get_beverage_data(parser: FileParser, data_path: str) -> dict:
    beverage_data = parser.parse(data_path)
    return beverage_data


def get_ingredient_data(parser: FileParser, data_path: str) -> dict:
    ingredient_data = parser.parse(data_path)
    return ingredient_data


def get_size_data(parser: FileParser, data_path: str) -> dict:
    size_data = parser.parse(data_path)
    return size_data


def get_customer_data(parser: FileParser, data_path: str) -> dict:
    customer_data = parser.parse(data_path)
    return customer_data
