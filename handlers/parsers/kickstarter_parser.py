import requests
from bs4 import BeautifulSoup
from handlers.parsers.parser import Parser
from models import PageInfo
from fake_useragent import UserAgent
import websockets


class KickstarterParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)
        self.session = requests.Session()

    def get_page(self) -> str:
        headers = {"User-Agent": UserAgent().getRandom["useragent"]}
        responce = self.session.get(self.link, headers=headers)
        self.page = responce
        return self.page.text

    def parse_page(self) -> PageInfo:
        self.parse_websocket()

    def parse_websocket(self):
        ...
