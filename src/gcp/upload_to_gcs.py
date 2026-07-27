import os

from google.cloud import storage

from config.settings import (
    BUCKET_NAME,
    GOOGLE_APPLICATION_CREDENTIALS,
    PROCESSED_DATA_PATH,
)

from src.utils.logger import logger

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS


def upload_to_gcs():

    try:

        logger.info("Connecting to Google Cloud Storage")

        client = storage.Client()

        bucket = client.bucket(BUCKET_NAME)

        blob = bucket.blob("users_clean.csv")

        blob.upload_from_filename(PROCESSED_DATA_PATH)

        logger.info("Upload completed successfully")

    except Exception:

        logger.exception("Upload failed")

        raise


if __name__ == "__main__":
    upload_to_gcs()