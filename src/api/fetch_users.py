import requests
import pandas as pd

URL = "https://jsonplaceholder.typicode.com/users"

print("Connecting to API...")

response = requests.get(URL)

print(f"Status Code: {response.status_code}")

data = response.json()

df = pd.DataFrame(data)

print(df.head())

df.to_csv("data/raw/users.csv", index=False)

print("CSV saved successfully!")