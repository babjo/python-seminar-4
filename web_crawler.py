from bs4 import BeautifulSoup
from gevent import monkey
import sys
import gevent
import time
import urllib.request


def crawling_product_price(product_url):
    try:
        with urllib.request.urlopen(product_url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            product_title = soup.find(id='productTitle').get_text().strip()
            price = soup.find(id='priceblock_ourprice').get_text()
            print(product_title, price)
    except:
        crawling_product_price(product_url)


if __name__ == '__main__':
    concurrency = sys.argv[1:2] == ['-c']

    product_urls = [
        'https://www.amazon.com/LG-Electronics-OLED65E7P-65-Inch-Smart/dp/B01MZF7YUD',
        'https://www.amazon.com/LG-Electronics-75SJ8570-75-Inch-SUPER/dp/B01N5V18W6',
        'https://www.amazon.com/All-New-Element-4K-Ultra-HD-Smart-TV-Fire-TV-Edition-43-Inch/dp/B06XD4SXWD',
        'https://www.amazon.com/Sceptre-U518CV-UMS-Ultra-True-black/dp/B06Y26S3BC',
        'https://www.amazon.com/Vizio-SMART-23-54IN-RETURNS-D24H-E1/dp/B06XQW5FJH',
        'https://www.amazon.com/Hisense-55K22DG-55-Inch-1080p-120Hz/dp/B00GFHG1OQ',
        'https://www.amazon.com/Samsung-Electronics-UN65MU9000-65-Inch-Ultra/dp/B06XGCT2PQ',
        'https://www.amazon.com/Samsung-Electronics-UN65MU8000-65-Inch-Ultra/dp/B06X9VSZYM',
        'https://www.amazon.com/Element-ELEFW3916R-720p-Certified-Refurbished/dp/B01N8PPMRG',
        'https://www.amazon.com/Samsung-UN50J5000-50-Inch-1080p-Model/dp/B00WR28LLE'
    ]

    start_time = time.time()

    if concurrency:
        monkey.patch_all()
        threads = [gevent.spawn(crawling_product_price, product_url) for product_url in product_urls]
        gevent.joinall(threads)
    else:
        for product_url in product_urls:
            crawling_product_price(product_url)

    end_time = time.time()

    print('-' * 90)
    print(f"Results(concurrency is {'on' if concurrency else 'off'}): {end_time-start_time}s")
