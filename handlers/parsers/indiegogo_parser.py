from icecream import ic
import requests
from bs4 import BeautifulSoup
from handlers.parsers.parser import Parser
from models import PageInfo


class IndegogoParser(Parser):
    def __init__(self, link: str) -> None:
        self.link = link
        self.page = None

    def get_page(self) -> str:
        return Parser.get_page(self)

    def parse_page(self) -> PageInfo:
        ...
