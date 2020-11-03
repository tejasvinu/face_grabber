import os
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.parse, urllib.error

j=36000

for year in range(1962,2000):
    y = 2020-year
    os.mkdir(str(y))
    os.chdir('C:/Users/tejasvinu/Desktop/python/celeb_faces/'+str(y)+'')
    for page in range(1,3000,50):
        url = 'https://www.imdb.com/search/name/?birth_year='+str(year)+'-01-01,'+str(year)+'-12-31&start='+str(page)+'&ref_=rlm'
        html = urllib.request.urlopen(url).read()
        soup = bs(html,'html.parser')
        img = soup.select('.lister-item-image')
        for i in img:
            print(i.contents)
            j=j+1
            for a in i.find_all('a'):
                x=str(j)
                if a.img:
                    m=a.img["src"]
                urllib.request.urlretrieve(m, 'c'+str(x)+'.jpg')
    os.chdir("C:/Users/tejasvinu/Desktop/python/celeb_faces")
print(j)
