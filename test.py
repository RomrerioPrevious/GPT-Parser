from handlers import GPT_Analysator
from icecream import ic

gpt = GPT_Analysator()
result = gpt.get_page_info_by_project_name("Nesty: Ultra Low Profile, Rugged Roof Top Tent")
ic(result)