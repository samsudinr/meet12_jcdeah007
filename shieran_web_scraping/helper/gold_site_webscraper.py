import requests
from bs4 import BeautifulSoup
import pandas as pd
from abc import ABC
from datetime import datetime
import os

class WebScraper(ABC):
    """
    Webscraper class:
    - connect with url
    - extract table
    - df to csv
    """
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url) 
        
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            print(f"HTML parsed succesfullly!")
        else:
            raise Exception(f"Failed connecting to site: {self.response.status_code}")

    def table_extract(self):
        if self.response:
            try:
                table = self.soup.find("table", class_="GoldPriceTable_table__iXXGg")

                headers_row = table.find("tr", class_="GoldPriceTable_header__SQL8m")
                self.headers = [th.get_text(strip=True) for th in headers_row.find_all("th")]

                self.rows = []
                for tr in table.find("tbody").find_all("tr"):
                    cells = [td.get_text(strip = True) for td in tr.find_all("td")]
                    if cells:
                        self.rows.append(cells)

                self.rows = self.rows[:-1] #lose strings/table text

                cleaned_rows = [[int(cell.replace(".","").replace("Rp","")) for cell in row] for row in self.rows]
                self.rows = cleaned_rows

            except Exception as e:
                raise 

    def to_csv(self):
        if not self.rows or not self.headers:
            raise Exception ("No data!")
        
        folder = "csv_data"
        os.makedirs(folder, exist_ok = True)
        
        date_string = datetime.now().strftime("%Y-%m-%d")
        file_path = os.path.join(folder, f"gold_price_{date_string}.csv")

        df = pd.DataFrame(self.rows, columns = self.headers)
        df.columns = [col.lower().strip().replace("-","") for col in df.columns]
        df.to_csv(file_path, index=False, encoding="utf-8")
        print(f"gold price {date_string} saved at {file_path}")
        return df
        




