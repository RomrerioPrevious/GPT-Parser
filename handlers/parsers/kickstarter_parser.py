from bs4 import BeautifulSoup
from handlers.parsers.parser import Parser
from models import PageInfo
from fake_useragent import UserAgent
from selenium import webdriver


class KickstarterParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)

    def get_page(self) -> str:
        ...

    def parse_page(self) -> PageInfo:
        ...

    def parse_websocket(self):
        ...
