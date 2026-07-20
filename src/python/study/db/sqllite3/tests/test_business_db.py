import logging
from config import path_settings
from config.logger import setup_logger
from src.database.connection import DatabaseConnection
from src.repositories.customer_repository import CustomerRepository


DB_NAME = str(path_settings.BUSINESS_DB_DIR)

def test_database_connection():

    setup_logger(log_level=logging.DEBUG)

    database_connection = DatabaseConnection(DB_NAME)
    assert database_connection
    assert database_connection.init_db()


def test_customer_repository():

    setup_logger(log_level=logging.DEBUG)
    db = DatabaseConnection(DB_NAME)

    customer_repo = CustomerRepository(db)

    customer_code = "0001"

    # 既存データ有無チェック
    row = customer_repo.get_by_code(customer_code)
    if (row is not None):
        # 既存データがあったら削除
        customer_repo.remove(customer_code)

    row_data = {
        "customer_code": customer_code,
        "name": "DDE",
        "email": "DDE@asteroid.sp",
        "phone": "090131314"
    }
    row_id = customer_repo.create(row_data)
