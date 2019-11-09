import urllib.request, urllib.error
from bs4 import BeautifulSoup

class ScrapingService:
    def __init__(self):
        # do nothing
        pass

    # Webから取得してスクレイピング
    def fetchAndScraping(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = res.read()

        soup = BeautifulSoup(body, 'html.parser')

        self.__execScraping(soup)

        return body

    # ファイルから読み込んでスクレイピング
    def fetchFromHtmlFileAndScraping(self, filePath):
        with open(filePath) as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

        self.__execScraping(soup)

    def __execScraping(self, soup):
        propertyList = soup.select('#prg-mod-bukkenList > div.prg-bundle')

        for aProperty in propertyList:
            print(aProperty)

