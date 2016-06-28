#!/usr/bin/env python

import urllib2
import re
import os
from bs4 import BeautifulSoup

def getLyrics(search)
    search = urllib.quote(search)
    soup = BeautifulSoup(urllib2.urlopen("http://www.songlyrics.com/index.php?section=search&searchW="+search).read())
