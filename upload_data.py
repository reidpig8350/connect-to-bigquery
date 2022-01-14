def upload_data(project_id="driven-stage-300605"):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"
    from google.cloud import bigquery as bq
    client = bq.Client(project_id)
    print("upload data")

upload_data()