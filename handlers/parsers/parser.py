from models import PageInfo
from selenium import webdriver
from fake_useragent import UserAgent


class Parser:
    def __init__(self, link: str):
        self.link: str = link
        self.page: str = ""
        self.driver = webdriver.Chrome(options=self.create_options())

    def create_options(self) -> webdriver.ChromeOptions:
        options = webdriver.ChromeOptions()
        options.page_load_strategy = "none"
        options.add_experimental_option("detach", True)
        options.add_argument("headless")
        options.add_argument(f"user-agent={UserAgent().random}")
        options.add_argument("--log-level=3")
        return options

    def get_page(self) -> str:
        ...

    def parse_page(self) -> PageInfo:
        ...

    def __del__(self):
        self.driver.quit()
        ic("driver will be closed")
