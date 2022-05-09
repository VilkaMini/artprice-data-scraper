import os
import string
import requests
from bs4 import BeautifulSoup
import typing
import pandas as pd

class Artscraper:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.cookies = {"lot-currency": "eur",
                        "ipp": "60"}
        self.url_add = "https://www.artprice.com"

    def scrape(self, start_page: int = 1, number_of_pages: int = 10) -> pd.DataFrame:
        """Scrapes website.

        Parameters:
            start_page (int): Start page number.
            number_of_pages (int): Number of pages to scrape.

        Returns:
            info (pd.DataFrame): dataframe with scraped information.
        """
        info = self.__get_full_array()
        array_of_keys = list(info.keys())

        # Loop through all pages
        for page in range(number_of_pages):
            URL = f"https://www.artprice.com/marketplace?idcurrencyzone=2&p={start_page+page}&sort=sort_dt-desc"
            page = self.__get_site(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            # Loop through all items in page
            for item in soup.find_all("div", class_="square"):
                # Get item webpage
                item_href = self.url_add + item.find("a")["href"]
                item_page = self.__get_site(item_href)
                item_soup = BeautifulSoup(item_page.content, "html.parser")
                # Get information from main page
                temp_dict = self.__get_array()
                temp_dict["link"] = item_href
                temp_dict["artist"] = self.__get_author(item)
                temp_dict["price"] = self.__get_price(item)
                # Get information from item page
                table = item_soup.find("table", class_="table classified_show")
                temp_dict = self.__get_table_rows(table, temp_dict)
                self.__append_to_full_array(temp_dict, info, array_of_keys)
        return pd.DataFrame(info)

    def __append_to_full_array(self, temp_d: dict, info: dict, keys: list):
        """Appends given temporary array to permanenet main information array.
        
        Returns:
            None
        """
        for key in keys:
            info[key].append(temp_d[key])
        return None

    def __get_table_rows(self, table: BeautifulSoup, temp_d: dict) -> dict:
        """Inserts information to coresponding temporary dictionary keys.
        
        Returns:
            temp_d: A dictionary with found information.
        """
        if table is None:
            return temp_d
        for row in table.find_all("tr"):
            print(row)
            try:
                sec_name = (row.find("td", class_="section").text).strip()
                sec_value = (row.find("td", class_="value").text).strip()
            except:
                break
            # Checking all possible keys
            if sec_name == "Title":
                temp_d["title"] = sec_value
            elif sec_name == "Year":
                temp_d["year"] = sec_value
            elif sec_name == "Category":
                temp_d["category"] = sec_value
            elif sec_name == "Medium":
                temp_d["medium"] = sec_value
            elif sec_name == "Signature":
                temp_d["signature"] = sec_value
            elif sec_name == "Size of the artwork":
                temp_d["size_of_artwork"] = sec_value
            elif sec_name == "Certificate issued by":
                temp_d["certificate_issued_by"] = sec_value
            elif sec_name == "Condition":
                temp_d["condition"] = sec_value
            elif sec_name == "Observations":
                temp_d["observations"] = sec_value
            elif sec_name == "Lot #":
                temp_d["id_number"] = sec_value
            elif sec_name == "Seller status":
                temp_d["seller_status"] = sec_value
            elif sec_name == "Country":
                temp_d["country"] = sec_value 
            elif sec_name == "Cost":
                temp_d["cost"] = sec_value
            elif sec_name == "Insurance":
                temp_d["insurance"] = sec_value
            elif sec_name == "Number of parcels":
                temp_d["number_of_parcels"] = sec_value
            elif sec_name == "Weight":
                temp_d["weight"] = sec_value
            elif sec_name == "Additional information":
                temp_d["add_information"] = sec_value
        return temp_d

    def __get_price(self, soup: BeautifulSoup) -> int:
        """Finds the item price on the website.
        
        Returns:
            item_price: A price value.
        """
        try:
            item_price = soup.find("div", class_="price").text
            item_price = int("".join(filter(str.isdigit, item_price)))
        except:
            item_price = None
        return item_price

    def __get_author(self, soup: BeautifulSoup) -> string:
        """Finds the item author name on the website.
        
        Returns:
            item_artist: An author name.
        """
        try:
            item_artist = soup.find("strong", class_="artist").text
        except:
            item_artist = None
        return item_artist


    def __get_full_array(self) -> dict:
        """Returns a dictionary containing keys to scraping information.
        
        Returns:
            iarray: A dictionary with keys to arrays to contain information.
        """
        iarray = {
            "artist": [],
            "title": [],
            "price": [],
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
            "link": []
        }
        return iarray

    def __get_array(self) -> dict:
        """Returns a dictionary containing keys to scraping information.
        
        Returns:
            iarray: A dictionary with keys to arrays to contain information.
        """
        iarray = {
            "artist": None,
            "title": None,
            "price": None,
            "type_of_artwork": None,
            "year": None,
            "category": None,
            "medium": None,
            "signature": None,
            "size_of_artwork": None,
            "cerfiticate_issued_by": None,
            "condition": None,
            "observations": None,
            "id_number": None,
            "seller_status": None,
            "country": None,
            "cost": None,
            "insurance": None,
            "number_of_parcels": None,
            "weight": None,
            "add_information": None,
            "link": None
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

    def scrape_to_file(self, start_page: int = 1, number_of_pages: int = 10 ) -> typing.TextIO:
        """Scrapes wbsite and creates a csv file with scraped information.

        Parameters:
            start_page (int): Start page number.
            number_of_pages (int): Number of pages to scrape.

        Returns:
            None (csv file).
        """
        df = self.scrape(start_page, number_of_pages)
        df.to_csv("Artprice_data.csv", encoding='utf-16')
        return None