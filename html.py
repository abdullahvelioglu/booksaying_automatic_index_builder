import urllib2
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup
file = open("index.html", "w")
for i in range(2,1759):
    string = 'http://booksaying.com/saying/detail/'+str(i)+'/'
    try:
        soup = BeautifulSoup(urllib2.urlopen(string).read())
        string = str(i)+')'+str(soup.body.p)+'\n'
        file.write(""+string+"")
    except urllib2.HTTPError:
        print str(i)+' Not Founded'
file.close()
