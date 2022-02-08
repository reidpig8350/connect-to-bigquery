from manipulate.make_copy import make_copy


if __name__=="__main__":

    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

    from datetime import datetime
    today = datetime.today().strftime("%Y%m%d")

    from manipulate import to_storage
    to_storage.upload_blob(today)

    from edit import create_table, upsert
    storage_file_name = "gs://jouney_message/history/JourneyMessageHistory_Others_{date}.csv" .format(date=today)
    create_table.upload_data(storage_file_name, today)

    upsert.upsert_table(today)