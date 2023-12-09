from dataclasses import dataclass


@dataclass
class PageInfo:
    name: str
    site: str
    in_amazon: str
    patent: bool
    can_buy: bool
    money: int
    usp: str
    unical_technology: str
    unical_in_world: str
    reviews: [str]
    risk: str
