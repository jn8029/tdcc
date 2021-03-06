# Taiwan Structured Product Information Crawler
![PyPI version](https://img.shields.io/pypi/pyversions/tdcc.svg)
![PyPI license](https://img.shields.io/pypi/l/tdcc.svg)
![Package Version](https://img.shields.io/pypi/v/tdcc.svg)
![Github Last Commit](https://img.shields.io/github/last-commit/jn8029/tdcc.svg)


This is a repository that offers a StructuredProductCrawler class to crawl [Taiwan TDCC](https://structurednotes.tdcc.com.tw/) website for the product information.

## Tutorial

```

from tdcc import StructuredProductCrawler
crawler = StructuredProductCrawler()
all_products = crawler.crawl()

```
```crawl()``` returns a Pandas DataFrame.
Data columns include:

| Column Name        | Are           |
| ------------- |:-------------:|
|URL| the product's partial url|
|UID| product id|
|NAME| product name|
|CURRENCY| product denomination|
|MATURITY| maturity date|
|UNDERLYING| underlying asset type|
|PRINCIPAL_PROTECTION| % of principal protection|
|PI| professional investor |
|ISSUE_DATE| issue date|
|ISSUER| issuer|
|MASTER_AGENT| master agent|
|DISTRIBUTOR| distributor|



## Installation
To install [this verson from PyPI](https://pypi.org/project/tdcc/), type:
```

pip install tdcc

```

To get the newest one from this repo (note that we are in the alpha stage, so there may be frequent updates), type:

```

pip install git+git://github.com/jn8029/tdcc.git

```

## To-do

TBC
