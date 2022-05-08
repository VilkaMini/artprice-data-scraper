# artprice-data-scraper

This repository contains Artprice.com scraper. It is designed to scrape data from Artprice.com and store it in pandas DataFrame object. 

## Functionality:

1. Using scrape() method to scrape a specified number of pages of art.
2. Using scrape_to_file() method to scrape a specified number of pages of art and return it in a csv file.

## Instalation:

Run the following line on command line to install the package:

```python
pip install git+https://github.com/VilkaMini/artprice-data-scraper
```

## Usage:

```python
from artscraper import Artscraper

# Create the scraper object
scraper = Artscraper()

# Provide starting page number and how many pages needs to be scraped (the example below will scrape pages 5-15)
df = scraper(5, 10)

# Or use package to get a file with scraped information
scraper_to_file(5, 15)
```

## Possible errors:

1. Could not reach the site. -> If the problem persists to not hesitate to contact me and I will try to implement solution.

## License

The MIT License (MIT). Please see the [license file](./LICENSE) for more information.