import requests
import locale

from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik_popular')
def detik_popular():
    url = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(url.text, 'html.parser')

    popular_area = soup.find(attrs={'class': 'grid-row list-content'})
    titles = popular_area.find_all(attrs={'class': 'media__title'})
    images = popular_area.find_all(attrs={'class': 'media__image'})

    return render_template('detik_scraper.html', images=images)

@app.route('/idr_rate')
def idr_rate():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr_rate.html', datas=json_data.values())

if __name__ == '__main__':
    app.run(debug=True)