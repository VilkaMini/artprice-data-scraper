import os
import string
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

class Artscraper:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.cookies = {"lot-currency": "eur"}
        self.url_add = "https://www.artprice.com"

    def scrape(self, start_page: int = 1, number_of_pages: int = 10):
        """Scrapes the artprice website for data"""
        info = self.__get_array()
        array_of_keys = list(info.keys())

        for page in range(number_of_pages):
            URL = f"https://www.artprice.com/marketplace?idcurrencyzone=2&p={start_page+page}&sort=sort_dt-desc"
            page = self.__get_site()
            soup = BeautifulSoup(page.content, "html.parser")

            # For everypage what to do






    def __get_array(self) -> dict:
        """Returns a dictionary containing keys to scraping information.
        
        Returns:
            iarray: A dictionary with keys to arrays to contain information.
        """
        iarray = {
            "artist": [],
            "title": [],
            "auction_price": [],
            "type_of_artwork": [],
            "year": [],
            "category": [],
            "medium": [],
            "signature": [],
            "size_of_artwork": [],
            "cerfiticate_issued_by": [],
            "condition": [],
            "observations": [],
            "id_number": [],
            "seller_status": [],
            "country": [],
            "cost": [],
            "insurance": [],
            "number_of_parcels": [],
            "weight": [],
            "add_information": [],
        }
        return iarray

    def __get_site(self, url: string) -> requests.Response():
        """Gets information from Artprice site.

        Returns:
            page (requests.Response): Object with information from site.
        """
        try:
            page = requests.get(url, headers=self.headers, cookies=self.cookies)
        except Exception as e:
            raise Exception("Could not reach the site") from e
        return page

    def __create_file(self, info: dict) -> int:
        """Creates a file with discount information.

        Parameters:
            info (dict): information dictionary.

        Returns:
            int (int): status that the file was created successfully.
        """
        if not os.path.exists('files'):
            os.mkdir('files')

        df = pd.DataFrame(info)
        df.to_csv(f"files/test", encoding='utf-16') # Needs some file management implementation
        return 0