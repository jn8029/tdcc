# -*- coding: utf-8 -*-
import pytest
from tdcc import SearchOptionParser, ProductListParser
import requests

index_url = "https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS210.jsp"
search_url = """https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS210.jsp?"""
query_params = [
    "AGENT_CODE={master_agent_id}",
    "ISSUE_ORG_UUID=",
    "SALE_ORG_UUID=",
    "FUND_LINK_TYPE=",
    "FUND_CURR=",
    "FUND_TYPE=",
    "FUND_STOP_DATE=",
    "agentDateStart=",
    "agentDateEnd=",
    "action=Q",
    "LAST_ORDER_BY=FUND_NAME",
    "ORDER_BY=",
    "IS_ASC=",
    "currentPage={page_number}"
]
@pytest.fixture(scope='session')
def search_option_parser():
    response = requests.get(index_url)
    parser = SearchOptionParser(response)
    yield parser

@pytest.fixture(scope='session')
def product_list_parser():
    credit_suisse = "A1520000"
    query_string = "&".join(query_params).format(master_agent_id= credit_suisse, page_number= 1)
    url = search_url + query_string
    response = requests.post(url)
    parser = ProductListParser(response)
    yield parser


class TestSearchOptionParser(object):
    def test_get_master_agents(self, search_option_parser):
        agents = search_option_parser.get_master_agents()
        assert len(agents) >= 23
    def test_get_distributors(self, search_option_parser):
        distro = search_option_parser.get_distributors()
        assert len(distro) >= 46

class TestProdcutListParser(object):
    def test_get_product_list(self, product_list_parser):
        product_list = product_list_parser.get_product_list()
        assert len(product_list)>=50
    def test_get_max_list_page(self, product_list_parser):
        assert 30 == product_list_parser.get_max_list_page()
