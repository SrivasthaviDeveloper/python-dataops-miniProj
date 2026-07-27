import os
import requests
import pandas as pd

from config.settings import API_URL, RAW_DATA_PATH
from src.utils.logger import logger


def fetch_users():

    try:

        logger.info("Fetching users from API")

        response = requests.get(API_URL)

        response.raise_for_status()

        users = response.json()

        df = pd.DataFrame(users)

        os.makedirs("data/raw", exist_ok=True)

        df.to_csv(RAW_DATA_PATH, index=False)

        logger.info(f"Successfully fetched {len(df)} users")

    except Exception:

        logger.exception("Failed while fetching users")

        raise


if __name__ == "__main__":
    fetch_users()