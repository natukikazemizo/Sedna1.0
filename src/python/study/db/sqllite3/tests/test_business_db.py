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
    row_data = {
        "customer_code": "0001",
        "name": "DDE",
        "email": "DDE@asteroid.sp",
        "phone": "090131314"
    }
    row_id = customer_repo.create(row_data)
