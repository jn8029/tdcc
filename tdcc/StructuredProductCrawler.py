from bs4 import BeautifulSoup
import requests
from .HtmlParser import SearchOptionParser

class StructuredProductCrawler:
    def __init__(self):
        self.index_url = "https://structurednotes-announce.tdcc.com.tw/Snoteanc/apps/bas/BAS210.jsp"
        self.product_url = search_page_url + "?fundUuid={fund_id}"
        self.search_url = """https://structurednotes-announce.tdcc.com.tw/Snoteanc
        /apps/bas/BAS210.jsp?AGENT_CODE={master_agent_id}}&
        ISSUE_ORG_UUID&SALE_ORG_UUID&FUND_LINK_TYPE&FUND_CURR&FUND_TYPE&FUND_STOP_DATE&
        agentDateStart&agentDateEnd&action=Q&LAST_ORDER_BY=FUND_NAME&
        ORDER_BY&IS_ASC&currentPage={page_number}"""

    def _get_master_agents(self):
        response = requests.get(self.index_url)
        parser = SearchOptionParser(response)
        return parser.get_master_agents()

    def get_all_products(self):
        pass
    
