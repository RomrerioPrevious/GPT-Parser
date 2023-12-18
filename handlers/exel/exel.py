import xlwt
from models import PageInfo


class Exel:
    workbook = None

    def __new__(cls):
        if not Exel.workbook:
            Exel.workbook = xlwt.Workbook()
        return cls

    def add_page(self, info: PageInfo):
        sheld = Exel.workbook.add_sheet(info.name)
        self.add_info(sheld, info)

    def add_has_info(self, value: str) -> str:
        if not value:
            return ""
        return value

    def add_info(self, sheld, info: PageInfo):
        sheld.write(1, 1, self.add_has_info(info.link))
        sheld.write(1, 2, self.add_has_info(info.link_of_image))
        sheld.write(1, 3, self.add_has_info(info.site))
        sheld.write(1, 4, self.add_has_info(info.in_amazon))
        sheld.write(1, 5, self.add_has_info(info.usp))
        sheld.write(1, 6, self.add_has_info(info.uniqueness_technology))
        sheld.write(1, 7, self.add_has_info(info.uniqueness_in_world))
        sheld.write(1, 8, self.add_has_info(info.reviews))
        sheld.write(1, 9, self.add_has_info(info.risks))
        sheld.write(1, 10, self.add_has_info(info.patent))
        sheld.write(1, 11, self.add_has_info(info.can_buy))
        sheld.write(1, 12, self.add_has_info(str(info.collecting)))

    def add_text(self, sheld):
        sheld.write(0, 1, "link")
        sheld.write(0, 2, "link_of_image")
        sheld.write(0, 3, "site")
        sheld.write(0, 4, "in_amazon")
        sheld.write(0, 5, "usp")
        sheld.write(0, 6, "uniqueness_technology")
        sheld.write(0, 7, "uniqueness_in_world")
        sheld.write(0, 8, "reviews")
        sheld.write(0, 9, "risks")
        sheld.write(0, 10, "patent")
        sheld.write(0, 11, "can_buy")
        sheld.write(0, 12, "collecting")

    def __del__(self):
        Exel.workbook.save("\\resources\\data\\result.xlsx")
