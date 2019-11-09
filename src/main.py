from googleApi import GoogleAPI
from scraping import ScrapingService
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
        print(aFile)
        # scrapingService.fetchFromHtmlFileAndScraping(aFile)

    # google = GoogleAPI()
    # contents = google.FetchDistanceFromGoogleApi()
    # print(contents)


if __name__ == "__main__":
    main()
