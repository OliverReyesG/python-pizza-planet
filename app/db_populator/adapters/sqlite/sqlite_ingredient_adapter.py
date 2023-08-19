from typing import List
from app.db_populator.adapters.base_adapter import BaseRepository
from app.db_populator.db.session import conn, cursor


class SQLiteIngredientAdapter(BaseRepository):

    def __init__(self) -> None:
        self.table_name = "ingredient"

    def create(self, data: dict) -> tuple:
        return super().create(data)

    def create_many(self, data: List[dict]) -> list:
        values = [(row["name"], row["price"]) for row in data]
        insert_query = f"INSERT INTO {self.table_name} (name, price) VALUES (?, ?)"
        response = cursor.executemany(insert_query, values)
        conn.commit()
        return response

    def list(self):
        list_query = f"SELECT * FROM {self.table_name}"
        response = cursor.execute(list_query).fetchall()
        return response
