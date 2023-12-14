import time

from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from handlers.parsers.parser import Parser
from models import PageInfo
from icecream import ic


class KickstarterParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)

    def get_page(self) -> str:
        ic("page is loading")
        page_is_loaded = False
        while not page_is_loaded:
            try:
                self.driver.get(self.link)
                time.sleep(2)
                if self.driver.title == "Access to this page has been denied.":
                    self.driver.quit()
                    self.driver = webdriver.Chrome(options=self.create_options())
                    raise ModuleNotFoundError
                page_is_loaded = True
            except ModuleNotFoundError:
                ...
        time.sleep(4)
        html = self.driver.find_element(by=By.TAG_NAME, value="html")
        for i in range(200):
            html.send_keys(Keys.DOWN)
        self.page = self.driver.page_source
        ic("page is loaded")
        return self.page

    def parse_page(self) -> PageInfo:
        page_info = PageInfo()
        soup = BeautifulSoup(self.page, "lxml")
        page_info.name = soup.find("a", class_="hero__link").text
        page_info.link = self.link
        page_info.link_of_image = soup.find("img", class_="js-feature-image")["src"]
        page_info.risks = [soup.find("div", class_="mb3 mb10-sm mb3 js-risks", id="risks-and-challenges")
                               .find("p", class_="js-risks-text text-preline")]
        page_info.collecting = self.collecting_to_int(soup.find("span", class_="money").text)
        return page_info

    def collecting_to_int(self, collecting: str) -> int:
        result = collecting.replace("€", "").replace(",", "")
        return int(result)

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")
