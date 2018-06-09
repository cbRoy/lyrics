#!/usr/bin/env python

import unittest
from lyrics.providers import Provider

class TestProvider(unittest.TestCase):

    test_host = Provider("songlist", "http://www.songlyrics.com/index.php?section=search&searchW=", [".serpresult h3 a","#songLyricsDiv"])
    
    def test_1(self):
        print self.test_host.host
    
    def test_2(self):
        print self.test_host.getLyrics('rag bone human')
        
if __name__ == '__main__':
    unittest.main();
