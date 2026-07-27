import os
from google.cloud import storage

from config.settings import (
    BUCKET_NAME,
    GOOGLE_APPLICATION_CREDENTIALS,
    RAW_DATA_PATH,
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS


def upload_to_gcs():
    try:
        print("Connecting to Google Cloud Storage...")

        print(f"Bucket: {BUCKET_NAME}")
        print(f"Uploading file: {RAW_DATA_PATH}")

        client = storage.Client()

        bucket = client.bucket(BUCKET_NAME)

        blob = bucket.blob("users.csv")

        blob.upload_from_filename(RAW_DATA_PATH)

        print("✅ File uploaded successfully!")

    except Exception as e:
        print(f"Upload failed: {e}")


if __name__ == "__main__":
    upload_to_gcs()