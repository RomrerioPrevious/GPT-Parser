from handlers.parsers import IndiegogoParser, KickstarterParser, Parser
from icecream import ic
from multiprocessing import RLock
from handlers.exel import Exel


class ProcessOfParsers:
    def __init__(self, link: str):
        ic.configureOutput(prefix="error | ")
        self.parser = self.find_class_of_link(link)

    @staticmethod
    def find_class_of_link(link: str) -> Parser:
        parsers = {"Indiegogo": IndiegogoParser,
                   "Kickstarter": KickstarterParser}
        site = link.replace("https://www.", "").split(".")[0].capitalize()
        return parsers[site](link)


def process_of_parser(link: str, path_of_result: str, lock: RLock()):
    try:
        parser = ProcessOfParsers.find_class_of_link(link)
        parser.get_page()
        info = parser.parse_page()
        with lock:
            ic(link)
            exel = Exel(path=path_of_result)
            exel.add_page(info)
            del exel
    except BaseException as error:
        ic(error)
