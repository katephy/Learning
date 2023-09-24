from bilibili.import_func import import_video
from readme.markdown import insert_lines_markdown
from bilibili.convert_info import info_text, add_record
import asyncio


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(add_record("BV1wy4y1D7JT", ["./basic.md", "./learnings/basic.md"], "React", True, range(37), "FRONT"))