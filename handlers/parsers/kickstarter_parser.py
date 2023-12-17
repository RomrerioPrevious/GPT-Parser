import time

from bs4 import BeautifulSoup
from openai import APIConnectionError
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from handlers import GPT_Analysator
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
        soup = BeautifulSoup(self.page, "lxml")
        if soup.find("h2", string="Upcoming Project"):
            page_info = self.parse_upcoming_project(soup)
        else:
            page_info = self.parse_project(soup)
        return page_info

    def parse_upcoming_project(self, soup) -> PageInfo:
        page_info = PageInfo()
        page_info.name = self.get_name(soup)
        page_info.link = self.link
        page_info.link_of_image = soup.find("img", class_="w100p block")["src"]
        page_info.risks = [""]
        page_info.reviews = [""]
        page_info.collecting = 0
        self.get_gpt_analysis(page_info)
        return page_info

    def parse_project(self, soup) -> PageInfo:
        page_info = PageInfo()
        page_info.name = self.get_name(soup)
        page_info.link = self.link
        page_info.link_of_image = soup.find("img", class_="js-feature-image")["src"]
        page_info.risks = [soup.find("div", class_="mb3 mb10-sm mb3 js-risks", id="risks-and-challenges")
                           .find("p", class_="js-risks-text text-preline")]
        page_info.collecting = self.collecting_to_int(soup.find("span", class_="money").text)
        page_info.reviews = [""]
        self.get_gpt_analysis(page_info)
        return page_info

    def get_gpt_analysis(self, page_info: PageInfo):
        try:
            gpt = GPT_Analysator()
            responce = gpt.get_page_info_by_project_name(page_info.name)
            page_info.site = responce["site"]
            page_info.in_amazon = responce["in_amazon"]
            page_info.usp = responce["usp"]
            page_info.uniqueness_technology = responce["uniqueness_technology"]
            page_info.uniqueness_in_world = responce["uniqueness_in_world"]
            page_info.patent = responce["patent"]
            page_info.can_buy = responce["can_buy"]
        except APIConnectionError:
            ...

    def get_name(self, soup):
        if soup.find("a", class_="hero__link"):
            name = soup.find("a", class_="hero__link").text
        elif soup.find("h2", class_="type-28 type-24-md soft-black mb1 project-name"):
            name = soup.find("h2", class_="type-28 type-24-md soft-black mb1 project-name").text
        elif soup.find("h1", class_="type-21 type-24-md type-28-lg kds-heading mb4 bold"):
            name = soup.find("h1", class_="type-21 type-24-md type-28-lg kds-heading mb4 bold").text
        else:
            name = ""
        return name

    def collecting_to_int(self, collecting: str) -> int:
        result = collecting.replace("€", "").replace(",", "").replace("$", "")
        return int(result)

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")
