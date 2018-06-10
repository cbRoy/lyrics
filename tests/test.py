#!/usr/bin/env python

import unittest
from lyrics.providers import Provider

class TestProvider(unittest.TestCase):

    def setUp(self):
        self.test_host = Provider("songlist", "http://www.songlyrics.com","/index.php?section=search&searchW=", [".serpresult h3 a","#songLyricsDiv"])
    
    def test_host_name(self):
        self.assertEqual(self.test_host.host, "songlist")
    
    def test_getLyrics(self):
        print self.test_host.getLyrics('rag bone human')
        
if __name__ == '__main__':
    unittest.main();
