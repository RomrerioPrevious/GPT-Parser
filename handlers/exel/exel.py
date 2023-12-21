from models import PageInfo
import openpyxl


class Exel:
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as file:
            file.read()
        self.workbook = openpyxl.load_workbook(path)

    def add_page(self, info: PageInfo):
        sheld = self.workbook.create_sheet(info.name[0:31])
        self.add_text(sheld)
        self.add_info(sheld, info)

    def add_has_info(self, value: str) -> str:
        if not value:
            return ""
        return value

    def add_info(self, sheld, info: PageInfo):
        sheld["A2"] = self.add_has_info(info.link)
        sheld["B2"] = self.add_has_info(info.link_of_image)
        sheld["C2"] = self.add_has_info(info.site)
        sheld["D2"] = self.add_has_info(info.in_amazon)
        sheld["E2"] = self.add_has_info(info.usp)
        sheld["F2"] = self.add_has_info(info.uniqueness_technology)
        sheld["G2"] = self.add_has_info(info.uniqueness_in_world)
        sheld["H2"] = self.add_has_info(" ".join(info.reviews))
        sheld["I2"] = self.add_has_info(" ".join(info.risks))
        sheld["J2"] = self.add_has_info(info.patent)
        sheld["K2"] = self.add_has_info(info.can_buy)
        sheld["L2"] = self.add_has_info(str(info.collecting))

    def add_text(self, sheld):
        sheld["A1"] = "link"
        sheld["B1"] = "link_of_image"
        sheld["C1"] = "site"
        sheld["D1"] = "in_amazon"
        sheld["E1"] = "usp"
        sheld["F1"] = "uniqueness_technology"
        sheld["G1"] = "uniqueness_in_world"
        sheld["H1"] = "reviews"
        sheld["I1"] = "risks"
        sheld["J1"] = "patent"
        sheld["K1"] = "can_buy"
        sheld["L1"] = "collecting"

    def __del__(self):
        self.workbook.save(self.path)
