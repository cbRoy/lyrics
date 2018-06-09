import urllib2
import re
from bs4 import BeautifulSoup

class Provider(object):
    
    # host = Provider('name',                   # site name
    #                 'www.provider.com',       # base address
    #                 '?search=',               # main search string
    #                 [                         # array of css patterns to scrape 
    #                   '.list td a',           # css selector for first result in search
    #                   '.lyrics div'           # css selector for lyrics 
    #                 ]
    #               )
    
    
    def __init__ (self, host, base, search, pattern):
        self.host = host
        self.base = base
        self.search = search
        self.pattern = pattern

    def _getRequest(self, url):
        return urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}) 

    def _getResult(self, url):
        request = self._getRequest (url)
        return BeautifulSoup(urllib2.urlopen( request ).read(),'lxml')

    def getLyrics(self, query):
        search = urllib2.quote(query)
        soup = self._getResult (self.base + self.search + search)
        firstResult = soup.select_one(self.pattern[0])['href']
        if(re.match(r'^http|www', firstResult) <= 0):   # if the host uses anchor hrefs such as "/lyrics/xxxxx"
               firstResult = self.base + firstResult    # add the base url infront of the first result href
        soup = self._getResult(firstResult)
        title = soup.title.string
        lyrics = soup.select_one(self.pattern[1]);
        return title, lyrics.get_text()    
