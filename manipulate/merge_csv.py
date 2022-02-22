import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("TPESE_KEY.json", scopes)
client = gspread.authorize(credentials)

sheet_keys = [
      "https://docs.google.com/spreadsheets/d/1zBPL_pnV4MvdeLPKC7V8-aHG8r263-oQhLVrOMZ4WYY/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1SOkE5Rhgj_8Gz4Z8CqxOI9gofkMmz4IQxepTFF5x4Zg/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1M0PoabiySfcbMUgKOMOKNLqQhKzWUBO4XoSVjonouc0/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1Bw2d3julQJlqMgyxKCjrIGE06vJp0puEEXkt3wNvf48/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1TknRLmk1_TlMOIH7KJ-3qAOR71lxQuh11G5HY8b-9gY/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1KOb7fPyRQhXZ8L6yrCjHa7OU6cxbrZ-CA1wMmZsbfFY/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1SuL6ZuRPOCtGDFx-nGur1wEfXevWPXBvdpt0B47Ek-U/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1Xu1BcJZijQl5_GZzuNom_6aSBwu8axGNC-KTQ7aCnLs/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1iOxtRznybSM_rCvJrzcCWWnrQ5Yz1rw5ezfDFbTUQiY/edit#gid=0",
      "https://docs.google.com/spreadsheets/d/1bh5u4SfsBsDvutfuhUw8EabFEQI7mFHFaZ84vqLDrvQ/edit#gid=0"
    ]


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

for sheet_url in sheet_keys:
    sheet_key = re.search(".*/d/(.*)/edit", sheet_url)[1]
    journey = client.open_by_key(sheet_key).sheet1
    if (not journey.get("A2")):
        print("skip")
        continue
    print(sheet_url)
    download(journey)