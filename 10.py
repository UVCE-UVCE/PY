import requests
from bs4 import BeautifulSoup as bs

url="https://en.wikipedia.org/wiki/Sachin_Tendulkar"

response=requests.get(url)
soup=bs(response.content,"html.parser")
images=soup.find_all('img')

for image in images:
    print(image.get("src"))
