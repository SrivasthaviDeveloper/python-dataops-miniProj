from src.utils.logger import logger
from src.validation.validate_data import validate_data
from src.api.fetch_users import fetch_users
from src.processing.clean_users import clean_users
from src.gcp.upload_to_gcs import upload_to_gcs


def main():

    logger.info("========== Pipeline Started ==========")

    fetch_users()

    clean_users()

    validate_data()

    upload_to_gcs()

    logger.info("========== Pipeline Completed ==========")


if __name__ == "__main__":
    main()