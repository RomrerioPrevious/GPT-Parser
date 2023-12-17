from dataclasses import dataclass


@dataclass
class PageInfo:
    name: str  # All
    link: str  # All
    link_of_image: str  # Kickstarter
    site: str # GPT
    in_amazon: str  # GPT
    usp: str  # GPT
    uniqueness_technology: str  # GPT
    uniqueness_in_world: str  # GPT
    reviews: [str]  # Indiegogo
    risks: [str]  # All
    patent: str  # GPT
    can_buy: str  # GPT
    collecting: int  # All

    def __init__(self):
        ...
