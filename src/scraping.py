import urllib.request, urllib.error
from bs4 import BeautifulSoup

class ScrapingService:
    def __init__(self):
        # do nothing
        pass

    def fetchAndScraping(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = res.read()

        return body
