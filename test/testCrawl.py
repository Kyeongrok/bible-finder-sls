from libs.crawler import crawl

url = "https://hetws2in6b.execute-api.ap-northeast-2.amazonaws.com/prod/v1/find/single/xml/창1:1"
pageString = crawl(url)
print(pageString)
