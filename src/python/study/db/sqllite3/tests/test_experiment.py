import logging
from config.logger import setup_logger
from src.experiment.basic import prepare_database


def test_prepare_database():
    setup_logger(log_level=logging.DEBUG)
    assert prepare_database()

