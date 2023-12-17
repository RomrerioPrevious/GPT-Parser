from models.page_info import PageInfo
from handlers.config import Config
from openai import OpenAI


class GPT_Analysator:
    def __init__(self):
        self.openai = OpenAI(
            api_key=Config().config["api"]
        )

    def get_page_info_by_project_name(self, project_name) -> {str: str}:
        result = {"site": "", "in_amazon": "", "usp": "",
                  "uniqueness_technology": "", "uniqueness_in_world": "",
                  "patent": "", "can_buy": ""}
        asks = self.get_asks(project_name)
        for i in asks:
            result[i] = self.parse_ask(asks[i])
        return result

    def parse_ask(self, ask: str) -> str:
        completion = self.openai.chat.completions.create(
            messages=[
                {"role": "user", "content": ask}
            ],
            model="gpt-4",
        )
        return completion.choices[0].message.content

    def get_asks(self, project) -> {str: str}:
        asks = {"site": f"Project '{project}' have site? If 'yes' which one is it, else say 'no'.",
                "in_amazon": f"I can buy '{project}' on amazon? Say yes or no.",
                "usp": f"Say me a unique selling point of '{project}'.",
                "uniqueness_technology": f"Is '{project}' a unique technology?",
                "uniqueness_in_world": f"How '{project}' unique is it in the world?",
                "patent": f"Project '{project}' has patent?",
                "can_buy": f"The product '{project}' can be purchased or a sample can be ordered in addition to the "
                           f"crowdfunding company?"}
        return asks
