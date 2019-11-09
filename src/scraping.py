import urllib.request, urllib.error
from bs4 import BeautifulSoup
from models import PropertyData

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

        properties = []
        for aProperty in propertyList:
            # 物件名
            propertyName = aProperty.select_one('div.moduleInner.prg-building > div.moduleHead > h2 > a > span.bukkenName.prg-detailLinkTrigger')
            if propertyName is not None:
                # 物件名が取れている

                # 住所
                targetAddress = aProperty.select_one('div.moduleInner.prg-building > div.moduleBody > div.sec-spec > div.sec-specB > div > table > tbody > tr:nth-child(1) > td').text

                # url
                url = aProperty.select_one('div.moduleInner.prg-building > div.moduleHead > h2 > a')['href']

                propetyData = PropertyData.PropertyData(
                    propertyName.text,
                    targetAddress,
                    url
                )

                properties.append(propetyData)

        return properties
