# initialize project
import os
import string
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./bigquery_key.json"
from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

# logging config.
import logging
log_file_route = '/Users/ssk/Desktop/bq_log.log'
with open(log_file_route, 'a') as file:
    file.write("\n\n＝＝＝＝＝＝＝＝＝＝＝＝＝＝\n")
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename=log_file_route, filemode='a', format=FORMAT)

# import modules
from manipulate import to_storage, make_copy
from edit import create_table, upsert

def main():
    try:
        # Step 0. download csv files from google sheets, temp.
        from manipulate import merge_csv

        # Step 1. upload the csv files
        source_file_name="./JourneyMessageHistory_Others.csv" #route of local file
        bucket_name = "jouney_message" #storage bucketname
        destination_blob_name="history/JourneyMessageHistory_Others_{date}.csv" .format(date=today) #naming new file in cloud storage
        to_storage.upload_blob(today, source_file_name, bucket_name, destination_blob_name)

        # Step 2. create table in bigquery
        storage_file_name = "gs://{bucket}/{file_in_storage}" .format(bucket=bucket_name, file_in_storage=destination_blob_name) #table name in BQ
        create_table.upload_data(today, storage_file_name)

        # Step 3. edit source data 
        upsert.upsert_table(today) #upsert table according to the file today

        # Step 4. log
        logging.debug("Data Updated!{}" .format(today))

    except:
        log_message = 'Catch an exception.'
        print(log_message)
        logging.debug(log_message, exc_info=True)

if __name__=="__main__":
    main()
    