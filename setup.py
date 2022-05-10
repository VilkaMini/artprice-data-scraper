from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="artScrape",
    version="0.0.8",
    description="Artprice scraper if designed to be used to scrape data from Artprice.com",
    py_modules=["artscraper"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas>=1.1.0", "requests>=2.23.0", "beautifulsoup4>=4.9.0", "lxml>=4.8.0"],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VilkaMini/artprice-data-scraper",
    author="Vilius Alaunis",
    author_email="viliusalaunis@gmail.com",
)