from dataclasses import dataclass


@dataclass
class PageInfo:
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
