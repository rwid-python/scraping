import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(url.text, 'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})
titles = populer_area.find_all(attrs={'class': 'media__title'})
images = populer_area.find_all(attrs={'class': 'media__image'})

# for title in titles:
#     print(title.text)

for image in images:
    print(image.find('a').find('img')['title'])

# print(populer_area)