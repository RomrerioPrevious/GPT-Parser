import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from handlers.parsers.parser import Parser
from models import PageInfo


class IndiegogoParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)

    def get_page(self) -> str:
        headers = {"User-Agent": UserAgent().getRandom["useragent"]}
        self.page = requests.get(self.link, headers=headers)
        return self.page.text

    def parse_page(self) -> PageInfo:
        ...
