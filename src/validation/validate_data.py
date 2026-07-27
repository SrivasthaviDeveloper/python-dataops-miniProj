import pandas as pd

from config.settings import PROCESSED_DATA_PATH
from src.utils.logger import logger


def validate_data():

    logger.info("========== Data Validation Started ==========")

    # Read processed CSV
    df = pd.read_csv(PROCESSED_DATA_PATH)

    # Dataset information
    total_rows = len(df)
    total_columns = len(df.columns)

    logger.info(f"Total Rows: {total_rows}")
    logger.info(f"Total Columns: {total_columns}")

    print("\n========== DATA QUALITY REPORT ==========")
    print(f"Rows: {total_rows}")
    print(f"Columns: {total_columns}")

    # Missing values
    missing_values = df.isnull().sum()

    print("\nMissing Values:")
    print(missing_values)

    logger.info(f"Missing Values:\n{missing_values}")

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicate_rows}")
    logger.info(f"Duplicate Rows: {duplicate_rows}")

    # Duplicate IDs
    duplicate_ids = df["id"].duplicated().sum()

    print(f"Duplicate IDs: {duplicate_ids}")
    logger.info(f"Duplicate IDs: {duplicate_ids}")

    # Validate email format
    invalid_emails = df[~df["email"].astype(str).str.contains("@")]

    print(f"Invalid Emails: {len(invalid_emails)}")
    logger.info(f"Invalid Emails: {len(invalid_emails)}")

    # Required columns
    required_columns = [
        "id",
        "name",
        "username",
        "email"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        logger.error(f"Missing Required Columns: {missing_columns}")
        raise ValueError(
            f"Missing Required Columns: {missing_columns}"
        )

    print("Required Columns: OK")
    logger.info("Required Columns: OK")

    print("\n✅ Data Validation Passed")

    logger.info("========== Data Validation Completed ==========")


if __name__ == "__main__":
    validate_data()