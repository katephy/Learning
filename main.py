from bilibili.import_func import import_video
from readme.markdown import insert_lines_markdown
from bilibili.convert_info import info_text
import asyncio


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(import_video("BV1wy4y1D7JT"))
    insert_lines_markdown("./basic.md", "./README.md", info_text(result, "React", True, range(18)), "VIDEO")