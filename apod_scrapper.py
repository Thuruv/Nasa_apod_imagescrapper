import urllib
from bs4 import BeautifulSoup
from time import gmtime, strftime
import os

url = 'http://apod.nasa.gov/apod/'
soup = BeautifulSoup(urllib.urlopen(url).read())
try:
    temp = soup.img['src']
    myPath = # your Path in drive
    data = []
    full_url = url + temp
    title = (soup.body.b.text).strip('\n') + '.jpg'
    nasa = os.path.join(myPath, title)
    urllib.urlretrieve(full_url,nasa)
    details =  data.append((title , strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    with open('./apod_imagedb.txt','wb+') as f:
        f.write(str(data))
        f.close()
except TypeError:
    res =  'They Has No Image For Today. .! '
    print res
    with open('./apod_imagedb.txt','wb+') as f:
        f.write(str(res))
        f.close()
