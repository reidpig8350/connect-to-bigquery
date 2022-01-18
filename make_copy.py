# Make a Copy-------------------------
from datetime import datetime
today = datetime.today().strftime("%Y%m%d")

import shutil
import os

src = "D:\\Data\\SFMC\\JourneyMessageHistory_Others.csv"
dst = "D:\\Data\\SFMC\\history\\JourneyMessageHistory_Others{timestamp}.csv" .format(timestamp=today)

if not os.path.exists("D:\\Data\\SFMC\\history"):
    os.mkdir("D:\\Data\\SFMC\\history")
shutil.copyfile(src, dst)
# Make a Copy-------------------------