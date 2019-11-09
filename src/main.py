from googleApi import GoogleAPI
from scraping import ScrapingService
import sys

def main():
    args = sys.argv

    if len(args) < 2:
        print('argument is invalid')
        return ()

    scrapingService = ScrapingService()
    scrapingService.fetchAndScraping(args[1])

    # google = GoogleAPI()
    # contents = google.FetchDistanceFromGoogleApi()
    # print(contents)

if __name__ == "__main__":
    main()
