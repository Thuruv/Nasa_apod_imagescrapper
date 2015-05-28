import urllib
from bs4 import BeautifulSoup
from time import gmtime, strftime
import os

url = 'http://apod.nasa.gov/apod/'
soup = BeautifulSoup(urllib.urlopen(url).read())
temp = soup.img['src']
myPath = # your file path

full_url = url + temp
title = (soup.body.b.text).strip('\n') + '.jpg'
nasa = os.path.join(myPath, title)
urllib.urlretrieve(full_url,nasa)
details =  (title , strftime("%Y-%m-%d %H:%M:%S", gmtime()))

with open('/mypath/apod_imagedb.txt','wb+') as f:
    f.write(str(details))
    f.close()
