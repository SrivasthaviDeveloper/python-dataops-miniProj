import os
import requests
import pandas as pd

from config.settings import API_URL, RAW_DATA_PATH
from src.utils.logger import logger


def fetch_users():

    try:
        logger.info("Starting user data extraction...")

        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        logger.info(f"API Response Status: {response.status_code}")

        users = response.json()

        logger.info(f"Number of records received: {len(users)}")

        df = pd.DataFrame(users)

        os.makedirs("data/raw", exist_ok=True)

        df.to_csv(RAW_DATA_PATH, index=False)

        logger.info(f"CSV saved successfully at {RAW_DATA_PATH}")

        print(df.head())

        print("\nUsers successfully saved!")

    except requests.exceptions.Timeout:

        logger.error("Request timed out.")

        print("The API request timed out.")

    except requests.exceptions.ConnectionError:

        logger.error("Unable to connect to API.")

        print("Could not connect to the API.")

    except requests.exceptions.HTTPError as e:

        logger.error(f"HTTP Error: {e}")

        print("HTTP Error occurred.")

    except Exception as e:

        logger.exception("Unexpected Error")

        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    fetch_users()