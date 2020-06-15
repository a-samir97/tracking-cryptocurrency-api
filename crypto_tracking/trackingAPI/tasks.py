# tracking the cryptocurrecny using celery 
# crawling cryptocurrency using beautifulsoup4


# celery used for async tasks 
from celery import shared_task
from celery.schedules import crontab
from celery.decorators import periodic_task

# beautifulsoup used for scraping data
from bs4 import BeautifulSoup

# requests used for make a request (used get request in this example)
import requests
import time

from .models import Cryptocurrency

@shared_task
def start_crawling_cryptocurrency():
    requested_data = requests.get('https://coinranking.com/')
    bs = BeautifulSoup(requested_data.text, 'html.parser')

    # by this code we will get the first 10 rows of the table
    rows = bs.find('tbody', class_='table__body')
    rows = rows.find_all('tr', class_='table__row')[0:10]
    # looping for all rows 
    for row in rows:
        # get the cryptocurrency data
        cryptocurrency = row.find('span', class_='profile__name').get_text().strip().replace('\n', '')
        # get price and market cap values 
        values = row.find_all('div', class_='valuta')
        # values[0] is the value of the price
        # values[1] is the value of the market cap
        price = values[0].get_text().strip().replace('\n', '')
        market_cap = values[1].get_text().strip().replace('\n', '')
        # get change data
        change = row.find('div', class_='change').get_text().strip().replace('\n', '')
        # create a new object in the database
        obj, created = Cryptocurrency.objects.get_or_create(
            crypto_name=cryptocurrency,
            price=price,
            market_cap=market_cap,
            change=change
        )
    

@periodic_task(run_every=(crontab()), name="run_every_1_minute", ignore_result=True)
def update_data():
    requested_data = requests.get('https://coinranking.com/')
    bs = BeautifulSoup(requested_data.text, 'html.parser')

    # by this code we will get the first 10 rows of the table
    rows = bs.find('tbody', class_='table__body')
    rows = rows.find_all('tr', class_='table__row')[0:10]
    # looping for all rows 
    for row in rows:
        # get the cryptocurrency data
        cryptocurrency = row.find('span', class_='profile__name').get_text().strip().replace('\n', '')
        # get price and market cap values 
        values = row.find_all('div', class_='valuta')
        # values[0] is the value of the price
        # values[1] is the value of the market cap
        price = values[0].get_text().strip().replace('\n', '')
        market_cap = values[1].get_text().strip().replace('\n', '')
        # get change data 
        change = row.find('div', class_='change').get_text().strip().replace('\n', '')
        # update object in the database
        data = {
            'crypto_name': cryptocurrency,
            'price':price,
            'market_cap':market_cap,
            'change':change
        }
        Cryptocurrency.objects.filter(crypto_name=cryptocurrency).update(**data)

if not Cryptocurrency.objects.all():
    print("TEST")
    start_crawling_cryptocurrency()
