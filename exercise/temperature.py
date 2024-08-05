import requests
import selectorlib
import os
from datetime import datetime
import sqlite3

URL = 'https://programmer100.pythonanywhere.com/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("../data.db")


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('temp.yaml')
    value = extractor.extract(source)['temperature']
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return value, now


def store(temperature, date):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO temperatures VALUES(?,?)', (date, temperature))
    connection.commit()


if __name__ == '__main__':
    source = scrape(URL)
    temperature, date = extract(source)
    store(temperature, date)
    print(temperature, 'C, ', date)