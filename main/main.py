def make_copy(date):

    import shutil
    import os

    src = "D:\\Data\\SFMC\\JourneyMessageHistory_Others.csv"
    dst = "D:\\Data\\SFMC\\history\\JourneyMessageHistory_Others{timestamp}.csv" .format(timestamp=date)

    if not os.path.exists("D:\\Data\\SFMC\\history"):
        os.mkdir("D:\\Data\\SFMC\\history")
    shutil.copyfile(src, dst)

if __name__=="__main__":

    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

    from datetime import datetime
    today = datetime.today().strftime("%Y%m%d")
    make_copy(today)

    from manipulate import to_storage
    to_storage.upload_blob(today)

    from edit import create_table, upsert
    storage_file_name = "gs://jouney_message/history/JourneyMessageHistory_Others_{date}.csv" .format(date=today)
    create_table.upload_data(storage_file_name, today)

    upsert.upsert_table(today)
    