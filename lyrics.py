#!/usr/bin/env python

import sys
import pydoc
import urllib2
from bs4 import BeautifulSoup

def createRequest(url):
    return urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}) 

def getResult(url):
    request = createRequest (url)
    return BeautifulSoup(urllib2.urlopen( request ).read(),'lxml')

def getLyrics(search):
    search = urllib2.quote(search)
    url="http://www.songlyrics.com/index.php?section=search&searchW="+search;
    soup = getResult (url)
    firstResult = soup.select_one(".serpresult h3 a")['href']
    soup = getResult(firstResult)
    title = soup.title.string
    lyrics = soup.select_one('#songLyricsDiv');
    return title, lyrics.get_text()

def getSearch():
    return raw_input("Search: ")

args = sys.argv
search = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else getSearch()
title, lyrics = getLyrics(search)
#print("\033]30;%s\007" % title) #sets title of Konsole, doesn't change back though. find new solution TODO
pydoc.pager(title + '\n\n' + lyrics)
