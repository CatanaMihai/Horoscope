import json
from bs4 import BeautifulSoup
import requests


# Find which number corrisponds to the right sign
def find_num(val):
    # Load the data from the signs.json file
    with open('signs.json', 'r') as file:
        data = json.load(file)
    for key, value in data.items():
        if value == val:
            return key

# This function will be used after the find_num has been used as it needs the number that corrisponds to the sign passed by the user. It will then return the text value of the element 'p'
def get_text(sign_num):
    txt = requests.get(f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_num}')
    # Parse the HTML content
    txt_soup = BeautifulSoup(txt.text, 'html.parser')
    # Find the h1 element
    txt_h1 = txt_soup.find('p')
    # Extract the text
    txt_text = txt_h1.text
    return txt_text
