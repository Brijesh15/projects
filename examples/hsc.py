import requests
url = "https://docs.python.org/3/tutorial/index.html"
res = requests.get(url)
print(res.content)
