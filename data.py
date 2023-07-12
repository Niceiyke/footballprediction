from requests_html import HTMLSession
from bs4 import BeautifulSoup

session=HTMLSession()
r= session.get('https://www.oddsportal.com/football/england/premier-league-2022-2023/arsenal-wolves-M1w8YmqE/#1X2;2')

r.html.render(sleep=1,scrolldown=2)

soup=BeautifulSoup(r.html.html,"html.parser")

home=soup.find('p',class_="max-sm:w-full order-first max-mm:!order-last truncate min-mm:!ml-auto h-7 flex-center").text
fthg=soup.find('div',class_="flex flex-wrap w-full gap-2 text-gray-dark").text
away=soup.find('p',class_="truncate h-7 flex-center").text
ftag=soup.find('div',class_="flex-wrap gap-2 flex-center max-sm:mr-0 text-gray-dark").text


bms=soup.find_all('div',class_='flex text-xs border-b h-9 border-l border-r')

b365=[]

for i in bms:
        link=i.find('a')['href']
        if '/bet365/link' in link:
                ho=i.find_all('p',class_='height-content')[1].text
                do=i.find_all('p',class_='height-content')[2].text
                ao=i.find_all('p',class_='height-content')[3].text

                odd=[ho,do,ao]
                b365.append(odd)

print(b365)




