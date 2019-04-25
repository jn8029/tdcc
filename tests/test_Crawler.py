# -*- coding: utf-8 -*-
import pytest
from tdcc import StructuredProductCrawler

@pytest.fixture(scope='session')
def crawler():
    crawler = StructuredProductCrawler()
    yield crawler

class TestCrawler:
    def test_get_master_agents(self, crawler):
        agents = crawler._get_master_agents()
        assert len(agents) >= 23
    def test_get_max_pages_for_all_master_agents(self, crawler):
        agents = crawler._get_master_agents()
        max_pages = crawler._get_max_pages_for_all_master_agents()
        assert len(agents) == len(max_pages)
    def test_get_all_page_urls(self, crawler):
        all_page_urls = crawler._get_all_page_urls()
        assert len(all_page_urls) >= 450
    def test_crawl(self, crawler):
        product_list = crawler.crawl()
        assert len(product) >= 21766
    def test_get_product_info(self, crawler):
        test_url ='/Snoteanc/apps/bas/BAS290.jsp?fundUuid=17f92894:14f2e3f3cd2:-677b'
        info = crawler._get_product_info(test_url)
        print(info)
