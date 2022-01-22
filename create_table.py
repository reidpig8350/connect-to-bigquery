from google.cloud import bigquery as bq
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

def upload_data():
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

    uri = "gs://jouney_message/history/「1JourneyMessageHistory_Others」的副本 - 1月12日，上午7:14.csv"

    table_id = 'china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_{name}' .format(name = today)
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows." .format(destination_table.num_rows))

upload_data()