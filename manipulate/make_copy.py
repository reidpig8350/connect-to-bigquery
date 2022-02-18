from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

def make_copy(src = "D:\\Data\\SFMC\\JourneyMessageHistory_Others.csv", dst = "D:\\Data\\SFMC\\history\\JourneyMessageHistory_Others{timestamp}.csv" .format(timestamp=today)):
    import shutil
    import os

    if not os.path.exists("D:\\Data\\SFMC\\history"):
        os.mkdir("D:\\Data\\SFMC\\history")
    shutil.copyfile(src, dst)