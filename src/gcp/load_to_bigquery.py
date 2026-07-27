from google.cloud import bigquery

client = bigquery.Client()

table_id = "python-gcp-miniproj.python_dataops.users"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

with open("data/raw/users.csv", "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config,
    )

job.result()

print("Loaded data into BigQuery!")