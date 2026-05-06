import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []
    authors = []

    data = soup.find_all("div", class_="quote")

    for item in data:
        quote = item.find("span", class_="text").text
        author = item.find("small", class_="author").text

        quotes.append(quote)
        authors.append(author)

    df = pd.DataFrame({
        "Quote": quotes,
        "Author": authors
    })

    df.to_csv("quotes.csv", index=False)

    print("✅ Data saved to quotes.csv")
else:
    print("❌ Failed to fetch website")