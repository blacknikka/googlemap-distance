from scraping import *

def main():
    scraping = ScrapingService()
    contents = scraping.fetchFromWeb("https://google.com")
    print(contents)

if __name__ == "__main__":
    main()
