MERGE
    china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others T
USING
    china-airlines-338006.JourneyMessage.JourneyMessageHistory_Others_20220122 S
ON
    T.system_id = S.system_id
    WHEN NOT MATCHED THEN INSERT (`system_id`, `sent_date__c`, `content_name__c`, `journey_content__r_a_b_test__c`, `type__c`, `card_no__c`, `card_type__c`, `status__c`, `arrival_station__c`, `departure_station__c`, `pnr_number`, `utm_content__c`, `birthday_event_date`) VALUES (`system_id`, `sent_date__c`, `content_name__c`, `journey_content__r_a_b_test__c`, `type__c`, `card_no__c`, `card_type__c`, `status__c`, `arrival_station__c`, `departure_station__c`, `pnr_number`, `utm_content__c`, `birthday_event_date`)
    WHEN MATCHED
    THEN
    UPDATE
    SET
        status__c=s.status__c;