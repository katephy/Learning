from bilibili.import_func import import_video
from readme.markdown import insert_lines_markdown
from bilibili.convert_info import info_text, add_record
import asyncio

BASIC_LEARNING_MD = "./learnings/basic.md"
BASIC_MD = "./basic.md"
README_MD = "./README.md"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(add_record("BV1wy4y1D7JT", [BASIC_MD, BASIC_LEARNING_MD], "React", True, range(37), "REACT"))
    result = loop.run_until_complete(add_record("BV1Xy4y1v7S2", [README_MD, BASIC_LEARNING_MD], "TypeScript", True, range(1), "TYPESCRIPT"))
    result = loop.run_until_complete(add_record("BV1AP411s7D7", [README_MD, BASIC_LEARNING_MD], "SSM", True, [], "SSM"))
    result = loop.run_until_complete(add_record("BV1np4y1C7Yf", [README_MD, BASIC_LEARNING_MD], "Gulimall", True, [], "GULIMALL"))
    result = loop.run_until_complete(add_record("BV1Np4y1z7BU", [README_MD, BASIC_LEARNING_MD], "Design Pattern", True, [], "DESIGNPATTERN"))
    