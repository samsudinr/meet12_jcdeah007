from helper.gold_site_webscraper import WebScraper
from helper.postgres_connector import PostgresConnector
from helper.db_config import db

def main():
    url = "https://harga-emas.org/"
    print(f"Scraping from {url}...")
    scraper = WebScraper(url)
    scraper.table_extract()
    df = scraper.to_csv() #returns dataframe

    connector = PostgresConnector(**db)
    connector.load("gold_price", df)

if __name__ == "__main__":
    main()
