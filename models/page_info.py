from dataclasses import dataclass


@dataclass
class PageInfo:
    name: str
    link: str
    link_of_image: str
    site: str
    in_amazon: str
    patent: bool
    can_buy: bool
    money: int
    usp: str
    uniqueness_technology: str
    uniqueness_in_world: str
    reviews: [str]
    risk: str
