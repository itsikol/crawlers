from bs4 import BeautifulSoup
import requests
f1 = open("genrename.txt")
f = open("moviename.txt","w+")
for genre in f1:
    for i in range(1,1000):
        url=genre.strip()+"page/"+str(i)+"/"
        print (url + '\n \n')
        r = requests.get(url)
        if r.status_code != 404 :
            r = r.text
            soup = BeautifulSoup(r)
            tds = soup.find_all('h3',{'class':'title_grid'})
            for tdd in tds :
                li = tdd.get('title')
                li = str(filter(lambda x:ord(x)>31 and ord(x)<128,li)).strip()
                print li
                f.write(li+'\n')
        else :
            break
