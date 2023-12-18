import time
from icecream import ic, install
from view import *
from handlers import *


def main():
    install()
    ic.configureOutput(prefix="info | ")
    with open("resources\\assets\\Logo.txt", "r") as file:
        print(file.read())
    view = View()
    view.print_description()
    view.config()
    config = Config()
    links = read_links()
    controller = ControllerOfProcess(links)
    controller.run()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    delta = round(end - start, 1)
    ic(delta)

