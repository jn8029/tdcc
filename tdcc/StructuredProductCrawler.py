from bs4 import BeautifulSoup
import requests
from .HtmlParser import SearchOptionParser, ProductListParser
import threading

class StructuredProductCrawler:
    def __init__(self):
        self.index_url = "https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS210.jsp"
        self.product_url = self.index_url + "?fundUuid={fund_id}"
        self.max_pages = {}
        self.queries = [
            "AGENT_CODE={agent}",
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
        self.base_query_url = self.index_url + "?" + "&".join(self.queries)

    def _get_master_agents(self):
        response = requests.get(self.index_url)
        parser = SearchOptionParser(response)
        return parser.get_master_agents()
    def _get_max_page(self, url, agent):
        response = requests.get(url)
        max_page_number = ProductListParser(response).get_max_list_page()
        self.max_pages[agent]=max_page_number
    def _get_max_pages_for_all_master_agents(self):
        agents = list(self._get_master_agents().keys())
        threads = []
        for agent in agents:

            first_page_url = self.base_query_url.format(agent=agent, page_number =1)

            thread = threading.Thread(target = self._get_max_page, args=(first_page_url, agent,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return self.max_pages
    def _get_all_page_urls(self):
        max_pages = self._get_max_pages_for_all_master_agents()
        urls = []
        for agent, max_page in max_pages.items():
            agent_urls = [self.base_query_url.format(agent=agent, page_number =x) for x in range(1,max_page+1)]
            urls += agent_urls
        return urls
