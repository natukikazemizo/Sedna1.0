from .base import BaseRepository
from typing import Optional

class CustomerRepository(BaseRepository):

    def create(self, customer_data: dict) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO customers (customer_code, name, email, phone)
                VALUES (?, ?, ?, ?)
            """, (customer_data["customer_code"], customer_data["name"],
                  customer_data.get("email"), customer_data.get("phone")))
            conn.commit()
            return cursor.lastrowid

    def get_by_code(self, code: str) -> Optional[dict]:
        with self.db.get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM customers WHERE customer_code = ?", (code,)
            ).fetchone()
            return dict(row) if row else None

    def remove(self, code: str) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.execute("""
                DELETE FROM customers WHERE customer_code = ?
            """, (code,))
            conn.commit()
            return cursor.rowcount
