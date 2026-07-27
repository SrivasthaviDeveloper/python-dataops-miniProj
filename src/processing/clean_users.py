import os
import pandas as pd

from config.settings import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
)

from src.utils.logger import logger


def clean_users():

    try:

        logger.info("Cleaning data")

        df = pd.read_csv(RAW_DATA_PATH)

        df = df.drop_duplicates()

        df = df.dropna()

        os.makedirs("data/processed", exist_ok=True)

        df.to_csv(PROCESSED_DATA_PATH, index=False)

        logger.info("Processed CSV created successfully")

    except Exception:

        logger.exception("Data cleaning failed")

        raise


if __name__ == "__main__":
    clean_users()