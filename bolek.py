import requests
from bs4 import BeautifulSoup
url = 'https://www.divadlobolkapolivky.cz/program/' 
fullpage = requests.get(url)
soup = BeautifulSoup(fullpage.text, 'lxml')
dates = soup.find_all('div', class_='events-date')
plays = soup.find_all('h2', itemprop='name')
actors = soup.find_all('div', class_='events-info')
print('V divadle Bolka Polívky hrají tato představení:\n')
for i in range(0, len(plays)):
    print(dates[i].text[4:-1])
    print(plays[i].text)
    print(actors[i].text + '\n')
