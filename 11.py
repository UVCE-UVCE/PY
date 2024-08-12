import requests
from bs4 import BeautifulSoup as bs
url = "https://www.imdb.com/chart/top/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
print("Response: ", response)
soup = bs(response.content, "html.parser")
titles = soup.find_all("h3", class_="ipc-title__text")
metadata = soup.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item")
print(metadata)
years = [metadata[0]]
for i in range(1, 30):
    if i%3==0:
        years.append(metadata[i])

print("Movie Details")
for i in range(10):
    print("Title: ", titles[i].text)
    print("Year: ", years[i].text)



