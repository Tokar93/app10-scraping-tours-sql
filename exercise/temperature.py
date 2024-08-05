import requests
import selectorlib
import os
from datetime import datetime
import csv
import plotly.express as px
import streamlit as st

URL = 'https://programmer100.pythonanywhere.com/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('temp.yaml')
    value = extractor.extract(source)['temperature']
    return value

def store(extracted):
    if not os.path.exists('data_temp.txt'):
        with open('data_temp.txt', 'w') as file:
            file.write('time;temperature\n')
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('data_temp.txt', 'a') as file:
        file.write(f'{now};{extracted}\n')

source = scrape(URL)
extracted = extract(source)
store(extracted)

times, temperatures = [], []
with open('data_temp.txt', 'r') as file:
    data = csv.reader(file, delimiter=';')
    count = 0
    for row in data:
        if count == 0:
            columns = [row[0], row[1]]
            count += 1
        else:
            times.append(row[0])
            temperatures.append(row[1])

fig = px.line(x=times, y=temperatures,
              labels={'x': columns[0].title(), 'y': columns[1].title()})


st.header('Makapaka')
st.plotly_chart(fig)


