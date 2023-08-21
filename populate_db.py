import os

from app.db_seed.adapters.sqlite import SQLiteIngredientAdapter, SQLiteBeverageAdapter, SQLiteSizeAdapter, SQLiteOrderAdapter, SQLiteOrderDetailAdapter
from app.db_seed.generators import get_ingredient_data, get_beverage_data, get_size_data, get_customer_data, generate_random_orders, get_order_details
from app.db_seed.db.session import conn, cursor
from app.db_seed.parsers import JSONFileParser, CSVFileParser

working_dir = os.getcwd()
data_dir = f"{working_dir}/app/db_seed/data/"

json_parser = JSONFileParser()
csv_parser = CSVFileParser()

ingredient_adapter = SQLiteIngredientAdapter()
ingredient_data = get_ingredient_data(
    parser=json_parser, data_path=f"{data_dir}/ingredients.json")

beverage_adapter = SQLiteBeverageAdapter()
beverage_data = get_beverage_data(
    parser=json_parser, data_path=f"{data_dir}/beverages.json")

size_adapter = SQLiteSizeAdapter()
size_data = get_size_data(parser=csv_parser, data_path=f"{data_dir}/sizes.csv")

order_adapter = SQLiteOrderAdapter()

order_detail_adapter = SQLiteOrderDetailAdapter()

customer_data = get_customer_data(
    parser=json_parser, data_path=f"{data_dir}/customers.json")


ingredient_adapter.create_many(ingredient_data)
beverage_adapter.create_many(beverage_data)
size_adapter.create_many(size_data)

fetched_ingredients = ingredient_adapter.list()
fetched_beverages = beverage_adapter.list()
fetched_sizes = size_adapter.list()


random_orders = generate_random_orders(
    ingredients=fetched_ingredients, beverages=fetched_beverages, sizes=fetched_sizes, customers=customer_data, max_orders=50)


for order in random_orders:
    order_adapter.create(order)
    current_order_id = cursor.lastrowid
    order['_id'] = current_order_id
    order_details = get_order_details(order=order)
    order_detail_adapter.create_many(order_details)

print("Database population was completed successfully!")
cursor.close()
conn.close()
