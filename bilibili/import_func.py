from bilibili_api import video
import json
import datetime


async def import_video(bvid) -> dict:
    v = video.Video(bvid=bvid)
    info = await v.get_info()
    info["link"] = "https://www.bilibili.com/video/{}".format(info["bvid"])
    return info


def get_video_duration(info_dict) -> tuple:
    duration_sec = info_dict["duration"]
    time_str = str(datetime.timedelta(seconds=duration_sec))
    return duration_sec, time_str


def get_video_pages(info_dict) -> list:
    pages = info_dict["pages"]
    if not len(pages):
        return pages
    pages = [
        {
            "index": page["page"],
            "duration": get_video_duration(page),
            "title": page["part"],
            "link": "https://www.bilibili.com/video/{}?p={}".format(info_dict["bvid"], page["page"])
        } for page in pages
    ]
    pages = sorted(pages, key=lambda page: page["index"])
    return pages