import json
from docx import Document


class Config:
    config = {}

    def __new__(cls):
        if not Config.config:
            with open("settings.json") as file:
                Config.config = json.load(file)
        return cls


def read_links() -> [str]:
    result = []
    config = Config().config
    docx = Document(config["site_list_path"])
    paragraphs = docx.paragraphs
    for line in paragraphs:
        if not line.text[0:6] == "https:":
            continue
        result.append(line.text)
    return result
