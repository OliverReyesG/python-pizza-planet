from typing import List
import random
from app.common.utils import generate_random_range
from app.db_seed.parsers import FileParser


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


def generate_order(ingredients: List[tuple], beverages: List[tuple], size: tuple, customer: dict) -> dict:
    total_price = sum(ingredient[2] for ingredient in ingredients) + \
        sum(beverage[2] for beverage in beverages) + size[2]
    new_order = {"client_name": customer.get("client_name"), "client_dni": customer.get("client_dni"), "client_address": customer.get(
        "client_address"), "client_phone": customer.get("client_phone"), "total_price": round(total_price, 2), "ingredients": ingredients, "beverages": beverages, "size_id": size[0]}
    return new_order


def generate_random_orders(ingredients: List[tuple], beverages: List[tuple], sizes: List[tuple], customers: List[dict]) -> list:
    random_orders = []
    for customer in customers:
        for i in range(random.randint(1, 6)):
            ingredients_range = generate_random_range(
                max_value=len(ingredients))
            beverages_range = generate_random_range(max_value=len(beverages))
            random_orders.append(generate_order(ingredients=ingredients[ingredients_range[0]:ingredients_range[1]],
                                                beverages=beverages[beverages_range[0]
                                                    :beverages_range[1]],
                                                size=sizes[random.randint(0, len(sizes) - 1)], customer=customer))
    return random_orders


def get_order_details(order: dict) -> List[dict]:
    order_id = order.get('_id')
    beverages = order.get('beverages')
    ingredients = order.get('ingredients')
    order_details = []
    for beverage in beverages:
        order_details.append(
            {"order_id": order_id, "beverage_id": beverage[0], "ingredient_id": None, "beverage_price": beverage[2], "ingredient_price": None})
    for ingredient in ingredients:
        order_details.append({"order_id": order_id, "beverage_id": None,
                             "ingredient_id": ingredient[0], "beverage_price": None, "ingredient_price": ingredient[2]})
    return order_details
