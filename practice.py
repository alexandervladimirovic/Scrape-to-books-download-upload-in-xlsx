import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15"
}

def download(url):

    resp = requests.get(url, stream=True)
    r = open('/Users/alexanderbeloglazov/Desktop/image/' + url.split('/')[-1], 'wb')

    for value in resp.iter_content(1024 * 1024):
        r.write(value)
    r.close()


def get_url():
    
    for page in range(1, 51):

        url = f'http://books.toscrape.com/catalogue/page-{page}.html'
        responce = requests.get(url, headers=headers)
        soup = BeautifulSoup(responce.text, 'lxml')
        
        data = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

        for i in data:

            card_url = 'http://books.toscrape.com/catalogue/' + i.find('a').get('href')
            
            yield card_url

def array():

    for card_url in get_url():

        responce = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(responce.text, 'lxml')

        data = soup.find('article', class_='product_page')

        name = data.find('h1').text
        price = data.find('p', class_='price_color').text
        img_url = data.find('img').get('src').replace('../../', 'http://books.toscrape.com/')

        download(img_url)

        yield name, price, img_url

        

