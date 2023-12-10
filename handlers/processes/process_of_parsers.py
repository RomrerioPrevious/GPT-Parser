from handlers.parsers import IndiegogoParser, KickstarterParser, Parser
from models import PageInfo


class ProcessOfParsers:
    def __init__(self, link: str):
        self.parser = self.find_class_of_link(link)

    @staticmethod
    def find_class_of_link(link: str) -> Parser:
        parsers = {"Indiegogo": IndiegogoParser(link),
                   "Kickstarter": KickstarterParser(link)}
        site = link.replace("https://www.", "").split(".")[0].capitalize()
        return parsers[site]

    def process(self):
        page = self.parser.get_page()
        info = self.parser.parse_page()