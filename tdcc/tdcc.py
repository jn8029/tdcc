import requests
from bs

search_page_url = "https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS210.jsp"
product_page_url = search_page_url + "?fundUuid={fund_id}"

res =requests.get("https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS290.jsp?fundUuid=3d359807:163512f9892:-6dd1")

with open("test.html","w") as f:
    f.write(res.text)
