import time
from openai import APIConnectionError, PermissionDeniedError
from handlers.gpt import GPT_Analysator
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from handlers.parsers.parser import Parser
from models import PageInfo
from icecream import ic


class IndiegogoParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)
        ic.disable()

    def get_page(self) -> str:
        ic("page is loading")
        self.driver.get(self.link)
        while True:
            try:
                self.driver.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div["
                                               "1]/div/div/div[2]/div/div[2]/button").click()
                break
            except NoSuchElementException:
                time.sleep(1)
        html = self.driver.find_element(by=By.TAG_NAME, value="html")
        for i in range(500):
            html.send_keys(Keys.DOWN)
        self.page = self.driver.page_source
        ic("page is loaded")
        return self.page

    def parse_page(self) -> PageInfo:
        page_info = PageInfo()
        soup = BeautifulSoup(self.page, "lxml")
        page_info.name = soup.find("p", class_="closedCampaignCarousel-title t-h3--sansSerif").text
        page_info.link = self.link
        risks = []
        try:
            risk_block = soup.find("h3", string="Risks and challenges")
            if not risk_block:
                risk_block = soup.find("h3", string="Risks & Challenges")
            while risk_block.next.find("strong"):
                risk_block = risk_block.next
                risks.append(risk_block.text)
                if not risk_block.next:
                    break
        except BaseException:
            ...
        page_info.risks = risks
        page_info.collecting = self.collecting_to_int(
            soup.find("span", class_="basicsGoalProgress-amountSold t-h5--sansSerif t-weight--bold").text)
        page_info.reviews = self.get_reviews()
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
        except APIConnectionError as error:
            ic(error.type)
        except PermissionDeniedError as error:
            ic(error.type)

    def get_reviews(self):
        result = []
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div/a[4]/div").click()
        time.sleep(1)
        reveiws = self.driver.find_element(by=By.XPATH,
                                           value="/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/div/ul")
        reveiws = reveiws.find_elements(by=By.TAG_NAME,
                                        value="p")
        for review in reveiws:
            result.append(review.text)
        return result

    def collecting_to_int(self, collecting: str) -> int:
        result = collecting.replace("\n", "").replace(" ", "").replace("$", "").replace("\xa0", "").replace("€", "")
        return int(result)

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")

#       'ws://' + window.location.host + '/jb-server-page?reloadMode=RELOAD_ON_SAVE&' + 'referrer=' + encodeURIComponent(window.location.pathname)
