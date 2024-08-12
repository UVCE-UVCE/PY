import requests 
from bs4 import BeautifulSoup as bs
url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.imdb.com/chart/top/',
}

response = requests.get(url, headers=headers)
print("Response: ", response)
response=requests.get(url)

soup=bs(response.content,"html.parser")

print(soup)