# artprice-data-scraper

This repository contains Artprice.com scraper. It is designed to scrape data from Artprice.com and store it in pandas DataFrame object. 

## Functionality:

1. Using scrape() method to scrape a specified number of pages of art.
2. Using scrape_to_file() method to scrape a specified number of pages of art and return it in a csv file.

Scraping returns the following features:

    1. Artist name
    2. Title
    3. Price
    4. Type of Artwork
    5. Year
    6. Category
    7. Medium
    8. Signature
    9. Size of artwork
    10. Condition
    11. Observations
    12. Id number
    13. Seller status
    14. Country
    15. Cost of shipping
    16. Insurance
    17. Number of parcels
    18. Weight
    19. Additional information
    20. Link to the item
    
Since the scraper was working poorly I found out that adding 5 seconds pause between scraping batches of 5 pages helps to not get blocked on the the site, but that still could happen and if it happens please go to the website manually and click "I am not a robot" prompt :). After that the scraper should work just fine.


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

1. Could not reach the site. -> Check if you are not blocked on the site manually. Then try to rerun the scraper. If the problem persists to not hesitate to contact me and I will try to implement solution.

## License

The MIT License (MIT). Please see the [license file](./LICENSE) for more information.
