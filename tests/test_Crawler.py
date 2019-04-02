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
        print(len(product_list))
