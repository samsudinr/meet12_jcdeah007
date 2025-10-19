# Web Scraping to CSV & Postgres Local

This project scrapes gold prices from https://harga-emas.org, cleans, saves as CSV, and loads dataframe to local PostgresSQL Database. 

This project uses Python, requests, beautifulsoup4, pandas, psycopg2

File Structure:
│
├── helper/
│ ├── gold_site_webscraper.py #Scrape with Beautifulsoup
│ ├── postgres_connector.py #Connects to postgres local to load tables
│ ├── db_config.py # Database credentials (gitignored)
│
├── main_process/
│ └── main_script.py # Main process (scrape + save + load)
│
├── csv_data/ # Folder for generated CSVs
├── .gitignore
└── README.md

