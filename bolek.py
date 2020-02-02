import requests
from bs4 import BeautifulSoup
url = 'https://www.divadlobolkapolivky.cz/program/' # Current program page.
fullpage = requests.get(url) # It downloads full page.
soup = BeautifulSoup(fullpage.text, 'lxml') # Page without tags.
dates = soup.find_all('div', class_='events-date') # It searches for dates.
plays = soup.find_all('h2', itemprop='name') # It searches for plays.
actors = soup.find_all('div', class_='events-info') # It searches for actors.
print('V divadle Bolka Polívky hrají tato představení:\n')
for i in range(0, len(plays)): # Is executed as many times as there are plays.
    print(dates[i].text[4:-1])
    print(plays[i].text)
    print(actors[i].text + '\n')
