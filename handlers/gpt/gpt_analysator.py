from models.page_info import PageInfo
from handlers.config import Config
import openai


class GPT_Analysator:
    openai.api_key = Config().config["api"]

    def get_page_info_by_link(self, link) -> {str: str}:
        asks = []

    def parse_ask(self, ask: str):
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": ask}
            ]
        )
        return completion.choices[0].message.content
