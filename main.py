from icecream import ic
from view import *
from handlers import *


def main():
    with open("resources\\assets\\Logo.txt", "r") as file:
        print(file.read())

    parser = KikstarterParser(
        "https://www.kickstarter.com/projects/255929858/flying-tent-7-seconds-to-the-stars?ref=discovery_popular&term=tent")

    page = parser.get_page()

    with open("page.html", "w") as file:
        file.write(page)


if __name__ == "__main__":
    main()
