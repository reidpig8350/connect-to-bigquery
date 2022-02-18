from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

def upload_blob(date=today, source_file_name="D:\\Data\\SFMC\\JourneyMessageHistory_Others.csv",bucket_name = "jouney_message",  destination_blob_name="history/JourneyMessageHistory_Others_{date}.csv" .format(date=today)):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "jouney_message"
    # The path to your file to upload
    # source_file_name = ""
    # The ID of your GCS object
    # destination_blob_name = "history/JourneyMessageHistory_Others_{date}.csv" .format(date=date)

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )