from models import PageInfo
import requests
from fake_useragent import UserAgent


class Parser:
    def __init__(self, link: str):
        self.link = link
        self.page = None

    def get_page(self) -> str:
        headers = {"User-Agent": UserAgent().getRandom["useragent"]}
        self.page = requests.get(self.link, headers=headers)
        return self.page.text

    def parse_page(self) -> PageInfo:
        ...
