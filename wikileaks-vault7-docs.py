from bs4 import BeautifulSoup
import os
import regex as re
import requests
def get_link():
    mnf = open("letsee.txt","w+")
    r = requests.get('https://wikileaks.org/vault7/')
    soup = BeautifulSoup(r.text)
    trying = soup.find('div',{'class':'content'})
    anot = trying.find_all('div',{'class':'release'})
    for dk in anot:
        links = dk.find_all('div',{'class':'sidebar-item'})
        for monkeys in links:
            fsd = monkeys.find('a').get('href')
            if re.search('#',fsd) == None:
                mnf.write("https://wikileaks.org/vault7"+fsd[1:]+fsd[11:-1]+'.pdf'+'\n')
    mnf.close()
def download_all():
    f = open("letsee.txt","r")
    for i in f.readlines():
        print i.rstrip('\n')
        print os.system("wget %s"%i.rstrip('\n'))

#get_link()
#download_all()
