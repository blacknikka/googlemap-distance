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

        return self.__execScraping(soup)

    # ファイルから読み込んでスクレイピング
    def fetchFromHtmlFileAndScraping(self, filePath):
        with open(filePath) as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

        return self.__execScraping(soup)

    # テキストからスクレイピングを行う
    def __execScraping(self, soup):
        propertyList = soup.select('#prg-mod-bukkenList > div.prg-bundle > div')

        addresses = []
        for aProperty in propertyList:
            targetAddress = aProperty.select('div.moduleInner.prg-building > div.moduleBody > div.sec-spec > div.sec-specB > div > table > tbody > tr:nth-child(1) > td')
            if len(targetAddress) > 0:
                addresses.append(targetAddress[0].text)

        return addresses
