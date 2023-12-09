from models import PageInfo


class Parser:
    def __init__(self, link: str) -> None:
        ...

    def get_page(self) -> None:
        ...

    def parse_page(self) -> PageInfo:
        ...
