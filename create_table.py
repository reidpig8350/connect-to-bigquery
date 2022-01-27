import re
from google.cloud import bigquery as bq
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

def upload_data(uri, date):
    client = bq.Client()
    job_config = bq.LoadJobConfig(
        schema=[
            bq.SchemaField('system_id', 'STRING'),
            bq.SchemaField('sent_date__c', 'STRING'),
            bq.SchemaField('content_name__c', 'STRING'),
            bq.SchemaField('journey_content__r_a_b_test__c', 'STRING'),
            bq.SchemaField('type__c', 'STRING'),
            bq.SchemaField('card_no__c', 'STRING'),
            bq.SchemaField('card_type__c', 'STRING'),
            bq.SchemaField('status__c', 'STRING'),
            bq.SchemaField('arrival_station__c', 'STRING'),
            bq.SchemaField('departure_station__c', 'STRING'),
            bq.SchemaField('pnr_number', 'STRING'),
            bq.SchemaField('utm_content__c', 'STRING'),
            bq.SchemaField('birthday_event_date', 'STRING')
        ],  
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bq.SourceFormat.CSV,
    )

    # uri = "gs://jouney_message/history/「JourneyMessageHistory_Others」的副本 - 10月6日，上午7/12.csv"

    table_id = 'china-airlines-338006.JourneyMessage_records.JourneyMessageHistory_Others_{name}' .format(name = date)
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows." .format(destination_table.num_rows))


journey_list = os.listdir('/Users/ssk/Desktop/other-upsert/history')
journey_list = ['「1JourneyMessageHistory_Others」的副本 - 1月27日，上午7:17.csv']

for journey_name in journey_list:
    if journey_name=='.DS_Store':
        continue
    year_reexp = re.search(" (.*年*).*", journey_name)[1]
    date = (re.search(".* \- (.*月.*日).*csv",journey_name)[1])
    date = date.replace("月", "m").replace("日", "d").replace(year_reexp, "")
    upload_data("gs://jouney_message/history/"+journey_name, date)