#!/usr/bin/env python

import sys
import pydoc
import urllib2
from bs4 import BeautifulSoup

def getLyrics(search):
    search = urllib2.quote(search)
    soup = BeautifulSoup(urllib2.urlopen("http://www.songlyrics.com/index.php?section=search&searchW="+search).read(),'lxml')
    firstResult = soup.select_one(".serpresult h3 a")['href']
    soup = BeautifulSoup(urllib2.urlopen(firstResult).read(),'lxml');
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
