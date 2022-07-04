# from bs4 import BeautifulSoup as bs 

# with open("test.html", "r", encoding="utf8") as f:
#     html = f.read()
#     soup = bs(html)
#     print(type(soup))

import requests
r=requests.get("https://reqbin.com/post-online", "r")
print(r.text)