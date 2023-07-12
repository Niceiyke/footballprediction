from requests_html import HTMLSession
from bs4 import BeautifulSoup

session=HTMLSession()
r= session.get('https://1xbet.whoscored.com/Matches/1640993/Preview/England-Premier-League-2022-2023-Newcastle-Leicester')
print(r.headers)

r.html.render(sleep=1,scrolldown=10)

soup=BeautifulSoup(r.html.html,"html.parser")

item=soup.find('div',class_='three-cols stat-info stat-bars-with-field-colors')

#matches=item.find('span',class_='overall-stat-value')
print(soup)

