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

import re

for the_key in sheet_keys:
    print(re.search(".*/d/(.*)/edit", the_key)[1])