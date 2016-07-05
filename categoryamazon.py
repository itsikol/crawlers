from bs4 import BeautifulSoup
import requests
f=open("catlink.txt","w+")
r=requests.get("http://www.amazon.in/gp/site-directory/ref=nav_shopall_fullstore")
data=r.text
soup=BeautifulSoup(data)
tbl = soup.find('table',{'id':'shopAllLinks'})
lis = tbl.find_all("li")
for tdd in lis:
  n = tdd.find('a').get('href')
  print n
  f.write('www.amazon.in'+n+'\n')
