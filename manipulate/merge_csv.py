import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("TPESE_KEY.json", scopes)
client = gspread.authorize(credentials)

sheet_keys = ['1zBPL_pnV4MvdeLPKC7V8-aHG8r263-oQhLVrOMZ4WYY', '1SOkE5Rhgj_8Gz4Z8CqxOI9gofkMmz4IQxepTFF5x4Zg']


file_path = './JourneyMessageHistory_Others.csv'

with open(file_path, "w", encoding="utf-8") as file:
    file.write("system_id,sent_date__c,content_name__c,journey_content__r_a_b_test__c,type__c,card_no__c,card_type__c,status__c,arrival_station__c,departure_station__c,pnr_number,utm_content__c,birthday_event_date\n")

def download(journey_name):
    values = journey_name.get("A:M")
    with open(file_path, "a", encoding="utf-8") as file:
        for j in range(1, len(values)):
            for k in range(0, 13):
                if k==12:
                    try:
                        if(values[j][k]=="0"):
                            file.write("\n")
                        elif(values[j][k]=="1"):
                            file.write("\n")
                        else:
                            file.write(values[j][k]+"\n")
                    except:
                        file.write("\n")
                        continue
                elif k<12:
                    try:
                        if(values[j][k]=="0"):
                            file.write(",")
                        elif(values[j][k]=="1"):
                            file.write(",")
                        else:
                            file.write(values[j][k]+",")
                    except:
                        file.write(",")
                        continue

journey_1 = client.open_by_key(sheet_keys[0]).sheet1
journey_2 = client.open_by_key(sheet_keys[1]).sheet1
download(journey_1)
download(journey_2)