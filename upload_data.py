from google.cloud import bigquery as bq

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

query = (
    '''
        CREATE TABLE `china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_{name}` (
            system_id STRING,
            sent_date__c STRING,
            content_name__c STRING,
            journey_content__r_a_b_test__c STRING,
            type__c STRING,
            card_no__c STRING,
            card_type__c STRING,
            status__c STRING,
            arrival_station__c STRING,
            departure_station__c STRING,
            pnr_number STRING,
            utm_content__c STRING,
            birthday_event_date STRING,
            iid STRING,
            date date,
            edm_sent INT,
            edm_bounce INT,
            edm_open INT,
            edm_click INT,
            app_open INT,
            app_success INT,
            app_fail INT,
            sms_delivered INT,
            sms_undelivered INT,
            trn_delivered INT,
            trn_sends INT,
            delivered_count INT,
            send_count INT,
            nfp_delivered INT,
            nfp_sends INT,
            trn_card_id_check STRING,
            nfp_card_id_check STRING
        );
    '''
    .format(name=today)
)


def upload_data(query=query, project_id="driven-stage-300605"):
    client = bq.Client()
    # query_job = client.query(query)
    # rows = query_job.result()
    # for row in rows:
    #     print(row)

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

    uri = "gs://journey_message/1JourneyMessageHistory_Others - 工作表1 (1).csv"

    table_id = 'china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_{name}' .format(name = today)
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows." .format(destination_table.num_rows))

upload_data()