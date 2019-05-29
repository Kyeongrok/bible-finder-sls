from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "https://hetws2in6b.execute-api.ap-northeast-2.amazonaws.com/prod/v1/find/single/xml/{}".format("요1:1")

pageString = crawl(url)
bsObj = BeautifulSoup(pageString, "html.parser")
print(bsObj)

