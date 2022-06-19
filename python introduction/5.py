import bs4
import requests
request_guardian_detail = requests.get("https://www.theguardian.com/politics/2021/dec/17/tory-chair-north-shropshire-voters-have-given-us-a-kicking")
html_guardian_detail = request_guardian_detail.text
soup_guardian_detail = bs4.BeautifulSoup(html_guardian_detail, "lxml")
for x in soup_guardian_detail.find_all("div",{"data-component":"youtube-atom"}):
    x.find("iframe", {"scr": "True"})
    print(x)