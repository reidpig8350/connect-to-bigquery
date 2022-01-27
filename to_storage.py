from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

client = storage.Client()
