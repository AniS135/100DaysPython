import requests as req
import json


Api_key = "32dc6f832e6e44dfac73d7efd50bc63e"

while True:
    keyword = input("Input category of news you want to search ('exit' if don't want to search further) :")

    if keyword == 'exit' :
        break

    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={Api_key}"

    res = req.get(url)

    news = json.loads(res.text)

    for article in news['articles']:
        print(article['title'])
        print(article['description'])
        print('------------------------------------------')




