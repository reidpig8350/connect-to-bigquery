query = (
    """
        MERGE
        GS_Data.JourneyMessageHistory_Others T
        USING
        GS_Data.JourneyMessageHistory_Others_tmp_ddo_61dfdb11590255348f5c81e0 S
        ON
        T.system_id = S.system_id
        WHEN NOT MATCHED THEN INSERT (`app_fail`, `app_open`, `app_success`, `arrival_station__c`, `birthday_event_date`, `card_no__c`, `card_type__c`, `content_name__c`, `date`, `delivered_count`, `departure_station__c`, `edm_bounce`, `edm_click`, `edm_open`, `edm_sent`, `iid`, `journey_content__r_a_b_test__c`, `nfp_card_id_check`, `nfp_delivered`, `nfp_sends`, `pnr_number`, `send_count`, `sent_date__c`, `sms_delivered`, `sms_undelivered`, `status__c`, `system_id`, `trn_card_id_check`, `trn_delivered`, `trn_sends`, `type__c`, `utm_content__c`) VALUES (`app_fail`, `app_open`, `app_success`, `arrival_station__c`, `birthday_event_date`, `card_no__c`, `card_type__c`, `content_name__c`, `date`, `delivered_count`, `departure_station__c`, `edm_bounce`, `edm_click`, `edm_open`, `edm_sent`, `iid`, `journey_content__r_a_b_test__c`, `nfp_card_id_check`, `nfp_delivered`, `nfp_sends`, `pnr_number`, `send_count`, `sent_date__c`, `sms_delivered`, `sms_undelivered`, `status__c`, `system_id`, `trn_card_id_check`, `trn_delivered`, `trn_sends`, `type__c`, `utm_content__c`)
        WHEN MATCHED
        THEN
        UPDATE
        SET
        app_fail = S.app_fail,
        app_open = S.app_open,
        app_success = S.app_success,
        arrival_station__c = S.arrival_station__c,
        birthday_event_date = S.birthday_event_date,
        card_no__c = S.card_no__c,
        card_type__c = S.card_type__c,
        content_name__c = S.content_name__c,
        date = S.date,
        delivered_count = S.delivered_count,
        departure_station__c = S.departure_station__c,
        edm_bounce = S.edm_bounce,
        edm_click = S.edm_click,
        edm_open = S.edm_open,
        edm_sent = S.edm_sent,
        iid = S.iid,
        journey_content__r_a_b_test__c = S.journey_content__r_a_b_test__c,
        nfp_card_id_check = S.nfp_card_id_check,
        nfp_delivered = S.nfp_delivered,
        nfp_sends = S.nfp_sends,
        pnr_number = S.pnr_number,
        send_count = S.send_count,
        sent_date__c = S.sent_date__c,
        sms_delivered = S.sms_delivered,
        sms_undelivered = S.sms_undelivered,
        status__c = S.status__c,
        system_id = S.system_id,
        trn_card_id_check = S.trn_card_id_check,
        trn_delivered = S.trn_delivered,
        trn_sends = S.trn_sends,
        type__c = S.type__c,
        utm_content__c = S.utm_content__c;
    """
)

def upload_data(query, project_id="driven-stage-300605"):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_key.json"
    from google.cloud import bigquery as bq
    client = bq.Client(project_id)
    print("upload data")
    query_job = client.query(query)