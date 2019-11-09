from googleApi import GoogleAPI
from scraping import ScrapingService
import settings
import sys
import glob
import os


def main():
    args = sys.argv

    if len(args) < 2:
        print('argument is invalid')
        return ()

    scrapingService = ScrapingService()
    files = glob.glob(os.path.join(args[1], '*.html'))

    for aFile in files:
        # データ抽出
        properties = scrapingService.fetchFromHtmlFileAndScraping(aFile)
        for aPropaty in properties[:1]:
            print(aPropaty.toString())

            # use google api
            google = GoogleAPI()
            receivedDict = google.FetchDistanceFromGoogleApi(
                settings.DEPARTURE,
                aPropaty.address()
            )

            # 時間をセット
            aPropaty.setTimeByWalk(receivedDict['rows'][0]['elements'][0]['duration']['value'])

if __name__ == "__main__":
    main()
