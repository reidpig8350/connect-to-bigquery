from google.cloud import bigquery as bq

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

query = (
    '''
        CREATE TABLE `china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_{name}` S
    '''
    .format(name=today)
)


def upload_data(query=query, project_id="driven-stage-300605"):
    client = bq.Client()
    query_job = client.query(query)
    rows = query_job.result()
    for row in rows:
        print(row)

def read_csv_file(csv_file_path="D:\\Data\\SFMC\\JourneyMessageHistory_Others.csv"):

    import pandas as pd
    schema = [
        bq.SchemaField('system_id STRING'),
        bq.SchemaField('sent_date__c STRING'),
        bq.SchemaField('content_name__c STRING'),
        bq.SchemaField('journey_content__r_a_b_test__c STRING'),
        bq.SchemaField('type__c STRING'),
        bq.SchemaField('card_no__c STRING'),
        bq.SchemaField('card_type__c STRING'),
        bq.SchemaField('status__c STRING'),
        bq.SchemaField('arrival_station__c STRING'),
        bq.SchemaField('departure_station__c STRING'),
        bq.SchemaField('pnr_number STRING'),
        bq.SchemaField('utm_content__c STRING'),
        bq.SchemaField('birthday_event_date STRING'),
        bq.SchemaField('iid STRING'),
        bq.SchemaField('date date'),
        bq.SchemaField('edm_sent INT'),
        bq.SchemaField('edm_bounce INT'),
        bq.SchemaField('edm_open INT'),
        bq.SchemaField('edm_click INT'),
        bq.SchemaField('app_open INT'),
        bq.SchemaField('app_success INT'),
        bq.SchemaField('app_fail INT'),
        bq.SchemaField('sms_delivered INT'),
        bq.SchemaField('sms_undelivered INT'),
        bq.SchemaField('trn_delivered INT'),
        bq.SchemaField('trn_sends INT'),
        bq.SchemaField('delivered_count INT'),
        bq.SchemaField('send_count INT'),
        bq.SchemaField('nfp_delivered INT'),
        bq.SchemaField('nfp_sends INT'),
        bq.SchemaField('trn_card_id_check STRING'),
        bq.SchemaField('nfp_card_id_check STRING')
    ]

    pd.read_csv(csv_file_path).to_sql

    

upload_data()