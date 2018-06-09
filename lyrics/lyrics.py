#!/usr/bin/env python

import sys
import pydoc
import string

from providers import Provider 

hosts = [
            Provider("songlist", "http://www.songlyrics.com","/index.php?section=search&searchW=", [".serpresult h3 a","#songLyricsDiv"]),
            Provider("lyricsmode","https://www.lyricsmode.com","/search.php?search=", [ '.songs_list tr:nth-of-type(1) .b' , '#lyrics_text'] ),
        ]


args = sys.argv
search = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else getSearch()


title, lyrics = hosts[1].getLyrics(search)

pydoc.pager(title + '\n\n' + lyrics)
