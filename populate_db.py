from typing import List
from app.db_populator.adapters.sqlite import SQLiteIngredientAdapter, SQLiteBeverageAdapter, SQLiteSizeAdapter
from app.db_populator.script import get_ingredient_data, get_beverage_data, get_size_data, get_customer_data

ingredient_adapter = SQLiteIngredientAdapter()
ingredient_data = get_ingredient_data()

beverage_adapter = SQLiteBeverageAdapter()
beverage_data = get_beverage_data()

size_adapter = SQLiteSizeAdapter()
size_data = get_size_data()

customer_data = get_customer_data()


# ingredient_response = ingredient_adapter.create_many(ingredient_data)
# beverage_response = beverage_adapter.create_many(beverage_data)
# size_response = size_adapter.create_many(size_data)

# print(ingredient_response)
# print(beverage_response)
# print(size_response)

ingredient_ids = [row[0] for row in ingredient_adapter.list()]
beverage_ids = [row[0] for row in beverage_adapter.list()]
size_ids = [row[0] for row in size_adapter.list()]


def generate_random_order(ingredient_ids: List[int], beverage_ids: List[int], size_ids: List[int], customer_list: List[dict]):
    pass


print(ingredient_ids, "\n")
print(beverage_ids, "\n")
print(size_ids, "\n")
