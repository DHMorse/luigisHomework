import requests

sites = {
    "Yahoo News" : "https://news.yahoo.com/",
    "Google News" : "https://news.google.com",
    "CNN" : "https://www.cnn.com/",
    "New York Times" : "https://www.nytimes.com/",
    "Fox News" : "https://www.foxnews.com/",
    "NBC News" : "https://www.nbcnews.com/",
    "Daily Mail" : "https://www.dailymail.co.uk/",
    "Washington Post" : "https://www.washingtonpost.com/",
    "Wall Street Journal" : "https://www.wsj.com/",
    "ABC News" : "https://abcnews.go.com/",
    "British Broadcasting Corporation" : "https://www.bbc.com/news"
}

term = input("Search for? ")

for newscorp, url in sites.items():
    html = requests.get(url)
    if term in html.text:
        print(f"{newscorp}: Yes")
    else:
        print(f"{newscorp}: No")
