import requests #pip install requests

query= input("What type of news are you interested in today?")
api = "Put your API key here"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-03-21&to=2026-03-21&sortBy=popularity&apiKey={api}"

print(url)
r = requests.get(url)

data=r.json()
articles = data["articles"]

for index, article in enumerate (articles):
    print(index + 1, article["title"], article["url"])
    print("\n*****************************************\n")