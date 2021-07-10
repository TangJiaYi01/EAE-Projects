import requests
from bs4 import *
import webbrowser

while True:

    url = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    beautifulsoup = BeautifulSoup(url.content, 'html.parser')
    header = beautifulsoup.find(id='firstHeading').text

    user_input = input('Would you like to view about ' + str(header)+'? (Yes or No) ')

    if user_input.upper() == 'YES':
        url = 'https://en.wikipedia.org/wiki/'+str(header)
        webbrowser.open(url)
        break

    elif user_input.upper() == 'NO':
        continue

    else:
        print('Choose yes or no...')
        continue



