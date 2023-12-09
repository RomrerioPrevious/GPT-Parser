from icecream import ic
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from handlers.parsers.parser import Parser
from models import PageInfo
from fake_useragent import UserAgent


class KikstarterParser(Parser):
    def __init__(self, link: str) -> None:
        self.link = link
        self.page = None

    def get_page(self) -> str:
        headers = {"User-Agent": UserAgent().getRandom["useragent"]}
        responce = HTMLSession().get(self.link, headers=headers)
        self.page = responce.text
        return self.page

    def parse_page(self) -> PageInfo:
        ...
