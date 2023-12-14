import time

from icecream import ic, install
from view import *
from handlers import *
from models import *


def main():
    install()
    ic.configureOutput(prefix="info | ")

    with open("resources\\assets\\Logo.txt", "r") as file:
        print(file.read())
    view = View()
    view.print_description()

    i = KickstarterParser("https://www.kickstarter.com/projects/255929858/flying-tent-7-seconds-to-the-stars?ref=discovery_popular&term=tent")
    i.get_page()
    i.parse_page()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    delta = round(end - start, 1)
    ic(delta)

#   "https://www.indiegogo.com/projects/the-crua-crucoon--2/pies"
#   "https://www.kickstarter.com/projects/255929858/flying-tent-7-seconds-to-the-stars?ref=discovery_popular&term=tent"
# /html/body/div/div/div[2]/div[2]/p
