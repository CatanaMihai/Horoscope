import requests

from bs4 import BeautifulSoup

# Gemini
# Fetch the webpage
gemini = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3')
# Parse the HTML content
gemini_soup = BeautifulSoup(gemini.text, 'html.parser')
# Find the h1 element
gemini_h1 = gemini_soup.find('p')
# Extract the text
gemini_text = gemini_h1.text

# Aries
# Fetch the webpage
aries = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1')
# Parse the HTML content
aries_soup = BeautifulSoup(aries.text, 'html.parser')
# Find the h1 element
aries_h1 = aries_soup.find('p')
# Extract the text
aries_text = aries_h1.text


# Taurus
# Fetch the webpage
taurus = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2')
# Parse the HTML content
taurus_soup = BeautifulSoup(taurus.text, 'html.parser')
# Find the h1 element
taurus_h1 = taurus_soup.find('p')
# Extract the text
taurus_text = taurus_h1.text


# Cancer
# Fetch the webpage
cancer = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4')
# Parse the HTML content
cancer_soup = BeautifulSoup(cancer.text, 'html.parser')
# Find the h1 element
cancer_h1 = cancer_soup.find('p')
# Extract the text
cancer_text = cancer_h1.text



# Leo
# Fetch the webpage
leo = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5')
# Parse the HTML content
leo_soup = BeautifulSoup(leo.text, 'html.parser')
# Find the h1 element
leo_h1 = leo_soup.find('p')
# Extract the text
leo_text = leo_h1.text



# Virgo
# Fetch the webpage
virgo = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6')
# Parse the HTML content
virgo_soup = BeautifulSoup(virgo.text, 'html.parser')
# Find the h1 element
virgo_h1 = virgo_soup.find('p')
# Extract the text
virgo_text = virgo_h1.text



# Libra
# Fetch the webpage
libra = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7')
# Parse the HTML content
libra_soup = BeautifulSoup(libra.text, 'html.parser')
# Find the h1 element
libra_h1 = libra_soup.find('p')
# Extract the text
llibra_text = libra_h1.text



# Scorpio
# Fetch the webpage
scorpio = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8')
# Parse the HTML content
scorpio_soup = BeautifulSoup(scorpio.text, 'html.parser')
# Find the h1 element
scorpio_h1 = scorpio_soup.find('p')
# Extract the text
scorpio_text = scorpio_h1.text


# Sagittarius
# Fetch the webpage
sagittarius = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9')
# Parse the HTML content
sagittarius_soup = BeautifulSoup(sagittarius.text, 'html.parser')
# Find the h1 element
sagittarius_h1 = sagittarius_soup.find('p')
# Extract the text
sagittarius_text = sagittarius_h1.text



# Capricorn
# Fetch the webpage
capricorn = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10')
# Parse the HTML content
capricorn_soup = BeautifulSoup(capricorn.text, 'html.parser')
# Find the h1 element
capricorn_h1 = capricorn_soup.find('p')
# Extract the text
capricorn_text = capricorn_h1.text



# Aquarius
# Fetch the webpage
aquarius = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11')
# Parse the HTML content
aquarius_soup = BeautifulSoup(aquarius.text, 'html.parser')
# Find the h1 element
aquarius_h1 = aquarius_soup.find('p')
# Extract the text
aquarius_text = aquarius_h1.text



# Pisces
# Fetch the webpage
pisces = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12')
# Parse the HTML content
pisces_soup = BeautifulSoup(pisces.text, 'html.parser')
# Find the h1 element
pisces_h1 = pisces_soup.find('p')
# Extract the text
pisces_text = pisces_h1.text