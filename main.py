import time
from icecream import ic, install
import os
from view import *
from handlers import *


def main():
    install()
    ic.configureOutput(prefix="info | ")
    with open("resources/assets/Logo.txt", "r") as file:
        print(file.read())
    view = View()
    view.print_description()
    view.config()
    config = Config()
    links = read_links()
    if config.config["result_path"][0] == "/":
        path = os.path.dirname(os.path.realpath(__file__))
        path += config.config["result_path"]
    else:
        path = config.config["result_path"]
    controller = ControllerOfProcess(links, path)
    controller.run()


def test():
    config = Config()
    gpt = GPT_Analysator()
    info = gpt.get_page_info_by_project_name("Beluga tent 6-in-1 from Qaou")
    ic(info)


if __name__ == "__main__":
    start = time.time()
    test()
    end = time.time()
    delta = round(end - start, 1)
    ic(delta)
