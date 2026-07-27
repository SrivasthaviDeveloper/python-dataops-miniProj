import os

from src.api.fetch_users import fetch_users
from config.settings import RAW_DATA_PATH


def test_fetch_users():

    fetch_users()

    assert os.path.exists(RAW_DATA_PATH)