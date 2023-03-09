import requests as req

# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

# res = req.get(url)
# # print(res.text)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(res.text, 'html.parser')

# for heading in soup.find_all("h2"):
#     print(heading.text)

# print(soup.prettify())

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1,
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

res = req.post(url, headers = headers, json = data)

print(res.text)