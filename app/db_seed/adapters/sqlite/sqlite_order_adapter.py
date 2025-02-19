from typing import List
from datetime import datetime
from app.db_seed.adapters.base_adapter import BaseRepository
from app.db_seed.db.session import conn, cursor
from app.common.utils import generate_random_date

class SQLiteOrderAdapter(BaseRepository):

    def __init__(self) -> None:
        self.table_name = "order"

    def create(self, data: dict) -> list:
        current_date = datetime.now()
        random_date = generate_random_date(min_year=2023, max_year=2023, max_month=current_date.month, max_day=current_date.day)
        values = (data["client_name"], data["client_dni"], data["client_address"],data["client_phone"], random_date, data["total_price"], data["size_id"])
        insert_query = f"INSERT INTO '{self.table_name}' (client_name, client_dni, client_address, client_phone, date, total_price, size_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
        response = cursor.execute(insert_query, values)
        conn.commit()
        return response

    def create_many(self, data: List[dict]) -> list:
        return super().create_many(data)

    def list(self):
        list_query = f"SELECT * FROM {self.table_name}"
        response = cursor.execute(list_query).fetchall()
        return response
