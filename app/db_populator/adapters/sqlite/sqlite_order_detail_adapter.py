from typing import List
from app.db_populator.adapters.base_adapter import BaseRepository
from app.db_populator.db.session import conn, cursor


class SQLiteOrderDetailAdapter(BaseRepository):

    def __init__(self) -> None:
        self.table_name = "order_detail"

    def create(self, data: dict) -> tuple:
        return super().create(data)

    def create_many(self, data: dict) -> list:
        values = [(row["order_id"], row["ingredient_id"], row["beverage_id"], row["ingredient_price"], row["beverage_price"]) for row in data]
        insert_query = f"INSERT INTO {self.table_name} (order_id, ingredient_id, beverage_id, ingredient_price, beverage_price) VALUES (?, ?, ?, ?, ?)"
        response = cursor.executemany(insert_query, values)
        conn.commit()
        return response

    def list(self):
        list_query = f"SELECT * FROM {self.table_name}"
        response = cursor.execute(list_query).fetchall()
        return response
