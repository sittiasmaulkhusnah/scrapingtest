import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.detik.com/"
headers = {"User-Agent": "Mozilla/5.0"}

#request
res = requests.get(url, headers=headers)
print(res.status_code)
print(res.content)

#beautifulsoap
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title
print(title)

#find all
title = soup.find_all("h3")
for item in title:
    print(item.get_text(strip=True))

#scraping to csv
titles = soup.find_all("li")

data = []

for item in titles:
    data.append(item.get_text(strip=True))

print(data)

df = pd.DataFrame(data, columns=["title"])
df.to_csv("detik.csv", index=False)