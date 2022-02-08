from google.cloud import bigquery as bq
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

def upload_data(date, uri):
    client = bq.Client()
    job_config_schema = bq.LoadJobConfig(
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

    table_id = 'china-airlines-338006.JourneyMessage_records.JourneyMessageHistory_Others_{date}' .format(date = date)
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config_schema
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {rows} rows." .format(rows = destination_table.num_rows))