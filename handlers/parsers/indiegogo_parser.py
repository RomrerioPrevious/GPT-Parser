import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from handlers.parsers.parser import Parser
from models import PageInfo


class IndiegogoParser(Parser):
    def __init__(self, link: str):
        super().__init__(link)

    def get_page(self) -> str:
        ic("page is loading")
        self.driver.get(self.link)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]/button").click()
        html = self.driver.find_element(by=By.TAG_NAME, value="html")
        for i in range(150):
            html.send_keys(Keys.DOWN)
        time.sleep(10)
        ic("page is loaded")
        return self.page

    def parse_page(self) -> PageInfo:
        page_info = PageInfo()
        soup = BeautifulSoup(self.page, "lxml")
        page_info.price = soup.find("span", class_="basicsGoalProgress-amountSold t-h5--sansSerif t-weight--bold").text
        return page_info

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")

#       'ws://' + window.location.host + '/jb-server-page?reloadMode=RELOAD_ON_SAVE&' + 'referrer=' + encodeURIComponent(window.location.pathname)
