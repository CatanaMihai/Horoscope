import json
from bs4 import BeautifulSoup
import requests

with open('signs.json', 'r') as file:
    data = json.load(file)

def get_text(sign_num):
    txt = requests.get(f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_num}')
    # Parse the HTML content
    txt_soup = BeautifulSoup(txt.text, 'html.parser')
    # Find the h1 element
    txt_h1 = txt_soup.find('p')
    # Extract the text
    txt_text = txt_h1.text
    return txt_text

def find_num(val):
    with open('signs.json', 'r') as file:
        data = json.load(file)
    for key, value in data.items():
        if value == val:
            return key