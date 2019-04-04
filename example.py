from tdcc import StructuredProductCrawler

if __name__ == "__main__":
    crawler = StructuredProductCrawler()
    all_products = crawler.crawl()
