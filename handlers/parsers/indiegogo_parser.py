import requests
from bs4 import BeautifulSoup
from handlers.parsers.parser import Parser
from models import PageInfo


class IndegogoParser(Parser):
    def __init__(self, link: str) -> None:
        super().__init__(link)

    def get_page(self) -> str:
        return super(IndegogoParser, self).get_page()

    def parse_page(self) -> PageInfo:
        ...
