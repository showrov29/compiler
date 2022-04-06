from bs4 import BeautifulSoup
import requests
import bs4
res=requests.get('https://www.aiub.edu/')
soup=BeautifulSoup(res.text,'lxml')
Title=soup.select('')
le=len(Title)
for x in range(0,le):
    print(Title[x].getText())