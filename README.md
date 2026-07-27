# Python DataOps Pipeline using Google Cloud Platform

## Project Overview

This project demonstrates an end-to-end DataOps pipeline using Python and Google Cloud Platform (GCP).

The pipeline extracts data from a REST API, cleans and validates it, stores it in Google Cloud Storage, and prepares it for analytics in BigQuery.

---

## Technologies Used

- Python
- Pandas
- Requests
- Google Cloud Storage
- BigQuery
- SQL
- Git
- GitHub
- GitHub Actions
- Pytest

---

## Architecture

```text
          REST API
              │
              ▼
      Python (Requests)
              │
              ▼
        Pandas Cleaning
              │
              ▼
      Data Validation
              │
              ▼
    Google Cloud Storage
              │
              ▼
         BigQuery Table
              │
              ▼
         SQL Analytics
```

## Folder Structure

```text
src/
    api/
    processing/
    validation/
    gcp/
    utils/
```

---

## Features

- REST API data ingestion
- Data cleaning using Pandas
- Data quality validation
- Google Cloud Storage integration
- BigQuery integration
- Logging
- Unit Testing
- CI/CD using GitHub Actions

---

## Sample Output

''' Pipeline Started

        ↓

    Fetching Users

        ↓

    Cleaning Data

        ↓

    Validation Passed

        ↓

    Uploaded Successfully

        ↓

    Pipeline Completed

---

## Future Improvements

- Airflow Scheduling
- Docker
- Cloud Functions
- Terraform
- Cloud Composer
- Monitoring Dashboard

---
# Python DataOps Pipeline using Google Cloud Platform

![Python CI](https://github.com/SrivasthaviDeveloper/python-dataops-miniProj/actions/workflows/python-ci.yml/badge.svg)