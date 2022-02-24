from google.cloud import bigquery as bq
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"

def delete_table(table_id):

    query=(
        '''
        DROP TABLE `{}`;
        '''
        .format(table_id)
    )

    client = bq.Client()
    query_job = client.query(query)

'''
"china-airlines-338006.JourneyMessage_records.JourneyMessageHistory_Others_{}"
'''