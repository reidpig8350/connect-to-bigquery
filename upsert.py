from datetime import datetime
today = datetime.today().strftime("%Y%m%d")


for day in range(1,27):
    query = (
        '''
        MERGE
            china-airlines-338006.JourneyMessage.JourneyMessage_Others T
        USING
            china-airlines-338006.JourneyMessage_records.JourneyMessageHistory_Others_{month}m{day}d S
        ON
            T.system_id = S.system_id
            WHEN NOT MATCHED THEN INSERT (`system_id`, `sent_date__c`, `content_name__c`, `journey_content__r_a_b_test__c`, `type__c`, `card_no__c`, `card_type__c`, `status__c`, `arrival_station__c`, `departure_station__c`, `pnr_number`, `utm_content__c`, `birthday_event_date`) VALUES (`system_id`, `sent_date__c`, `content_name__c`, `journey_content__r_a_b_test__c`, `type__c`, `card_no__c`, `card_type__c`, `status__c`, `arrival_station__c`, `departure_station__c`, `pnr_number`, `utm_content__c`, `birthday_event_date`)
            WHEN MATCHED
            THEN
        UPDATE
        SET
            status__c=s.status__c;
        '''
        .format(month=1, day=day)
    )

    print(day)

    def upsert_table(query=query):
        import os
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"
        from google.cloud import bigquery as bq

        client = bq.Client()
        query_job = client.query(query)
        rows = query_job.result()
        for row in rows:
            print(row)

    upsert_table()