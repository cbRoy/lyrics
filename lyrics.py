#!/usr/bin/env python

import sys
import pydoc
import urllib2
from bs4 import BeautifulSoup

def getLyrics(search):
    search = urllib2.quote(search)
    url="http://www.songlyrics.com/index.php?section=search&searchW="+search;
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}) 
    soup = BeautifulSoup(urllib2.urlopen( req ).read(),'lxml')
    firstResult = soup.select_one(".serpresult h3 a")['href']
    req = urllib2.Request(firstResult, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}) 
    soup = BeautifulSoup(urllib2.urlopen(req).read(),'lxml');
    title = soup.title.string
    lyrics = soup.select_one('#songLyricsDiv');
    return title, lyrics.get_text()

def getSearch():
    return raw_input("Search: ")

args = sys.argv
search = ' '.join(args[1:])
#search = getSearch()
title, lyrics = getLyrics(search)
print("\x1B]0;%s\x07" % title)
pydoc.pager(lyrics)
