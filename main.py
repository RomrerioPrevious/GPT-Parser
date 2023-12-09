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
#    parser = KickstarterParser(
#        "https://www.kickstarter.com/projects/255929858/flying-tent-7-seconds-to-the-stars?ref=discovery_popular&term=tent")
    parser = IndiegogoParser("https://www.indiegogo.com/projects/the-crua-crucoon--2/pies")
    page = parser.get_page()
    with open("page.html", "w") as file:
        file.write(page)


if __name__ == "__main__":
    main()
