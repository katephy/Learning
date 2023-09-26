from bilibili.import_func import import_video
from readme.markdown import insert_lines_markdown
from bilibili.convert_info import info_text, add_record
import json
import asyncio

BASIC_LEARNING_MD = "./learnings/basic.md"
BASIC_MD = "./basic.md"
README_MD = "./README.md"


if __name__ == "__main__":
    # Load learning record data
    with open("./data.json", "r") as f:
        data = json.load(f)

    loop = asyncio.get_event_loop()
    for idx, (label, obj) in enumerate(data.items()):
        title = obj["title"]
        bvid = obj["bvid"]
        paged = obj["paged"]
        finished = range(obj["finished"])
        basic_md = BASIC_MD if idx == 0 else README_MD
        loop.run_until_complete(add_record(bvid, [basic_md, BASIC_LEARNING_MD], title, paged, finished, label))