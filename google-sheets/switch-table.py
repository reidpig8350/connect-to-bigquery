import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
from datetime import date, datetime
now_str = datetime.now().strftime("%H")
import pandas as pd


def download(journey_name):

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("system_id,sent_date__c,content_name__c,journey_content__r_a_b_test__c,type__c,card_no__c,card_type__c,status__c,arrival_station__c,departure_station__c,pnr_number,utm_content__c,birthday_event_date\n")

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

def update_table(csv_file, target_table_url="https://docs.google.com/spreadsheets/d/1stuPZyyL1stbnOkUXw4QULle5LvKKKeJp40Smu3927Q/edit#gid=1131422765"):

    #initializing
    main_journey = client.open_by_key(target_table_url).sheet1
    main_journey.batch_clear(["A2:M"])

    update_speed = 10000

    update_data = pd.read_csv(csv_file, encoding="utf-8",
        dtype={'system_id': str,'sent_date__c': str,'content_name__c': str,'journey_content__r_a_b_test__c': str,'type__c': str,'card_no__c': str,'card_type__c': str,'status__c': str,'arrival_station__c': str,'departure_station__c': str,'pnr_number': str,'utm_content__c': str,'birthday_event_date': str})
    update_data = update_data.applymap(lambda x: "" if str(x)=="nan" else x)
    update_times = len(update_data.index)/update_speed
    print(update_times)

    #start updating
    for i in range(0, int(update_times)):
        update_range = "A{start}:M{end}" .format(start=2+i*update_speed, end=2+i*update_speed + update_speed)
        main_journey.update(update_range, update_data[i*update_speed: i*update_speed + update_speed].values.tolist())
        print(2+i*update_speed)
    

def switch_key():
    sheet_id = False
    if now_str == "07":
        return 0
    elif now_str == "09":
        return 1
    elif now_str == "10":
        return 2
    elif now_str == "11":
        return 3
    elif now_str == "12":
        return 4
    elif now_str == "13":
        return 5
    elif now_str == "14":
        return 6
    elif now_str == "15":
        return 7
    elif now_str == "16":
        return 8
    elif now_str == "17":
        return 9

if __name__=="__main__":

    # ------------- initialize -------------

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("TPESE_KEY.json", scopes)
    client = gspread.authorize(credentials)

    file_path = './JourneyMessageHistory_Others.csv'

    # main_sheet = ["https://docs.google.com/spreadsheets/d/1stuPZyyL1stbnOkUXw4QULle5LvKKKeJp40Smu3927Q/edit#gid=1131422765"]

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

    #open_google_sheet
    sheet_url = sheet_keys[switch_key()]
    sheet_key = re.search(".*/d/(.*)/edit", sheet_url)[1]
    which_journey = client.open_by_key(sheet_key).sheet1

    # ------------- initialize -------------

    # ------------- Main Program -------------
    print(switch_key())
    download(which_journey)
    update_table(file_path, "1bh5u4SfsBsDvutfuhUw8EabFEQI7mFHFaZ84vqLDrvQ")
    # ------------- Main Program -------------