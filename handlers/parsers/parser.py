from models import PageInfo
import requests
from fake_useragent import UserAgent
from icecream import ic


class Parser:
    def __init__(self, link: str) -> None:
        self.link = link
        self.page = None

    def get_page(self) -> str:
        headers = {"User-Agent": UserAgent().getRandom["useragent"]}
        responce = requests.get(self.link, headers=headers)
        self.page = responce.text
        return self.page

    def parse_page(self) -> PageInfo:
        ...
