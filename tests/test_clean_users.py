import os

from src.processing.clean_users import clean_users
from config.settings import PROCESSED_DATA_PATH


def test_clean_users():

    clean_users()

    assert os.path.exists(PROCESSED_DATA_PATH)