from icecream import ic
import rich


class View:
    def __init__(self, x: int = 0) -> None:
        self.x = x

    def __new__(cls, x):
        if not hasattr(cls, 'instance'):
            cls.instance = super(View, cls).__new__(cls)
        return cls.instance
