import time

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

    def get_page(self) -> str:
        ic("page is loading")
        self.driver.get(self.link)
        while True:
            try:
                self.driver.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]/button").click()
                break
            except NoSuchElementException:
                time.sleep(1)

        html = self.driver.find_element(by=By.TAG_NAME, value="html")
        for i in range(200):
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
        risk_block = soup.find("h3", string="Risks and challenges")
        while risk_block.next.find("strong"):
            risk_block = risk_block.next
            risks.append(risk_block.text)
        page_info.collecting = self.collecting_to_int(
            soup.find("span", class_="basicsGoalProgress-amountSold t-h5--sansSerif t-weight--bold").text)
        page_info.reviews = self.get_reviews()
        return page_info

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
        result = collecting.replace("\n", "").replace(" ", "").replace("$", "").replace("\xa0", "")
        return int(result)

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")

#       'ws://' + window.location.host + '/jb-server-page?reloadMode=RELOAD_ON_SAVE&' + 'referrer=' + encodeURIComponent(window.location.pathname)
