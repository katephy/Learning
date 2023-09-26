from bilibili.import_func import get_video_pages, get_video_duration, import_video
from chart.piechart import pie_chart
from readme.markdown import insert_lines_markdown
import asyncio


def info_text(info, video_title, pages=False, finished=[-1]) -> tuple:
    title = "\n\n### [{}]({})\n".format(video_title, info["link"])
    result = [title, "- Finished:\n"]
    
    if not pages:
        finished = ["\t- [ ]\n"]
        result.append(finished)
        return result
    
    pages_list = get_video_pages(info)
    minutes_total = round(get_video_duration(info)[0] / 60)

    pages_done = 0
    minutes_done = 0
    secs_done = 0
    for (idx, page) in enumerate(pages_list):
        if idx in finished:
            pages_done += 1
            secs_done += page["duration"][0]
    minutes_done = round(secs_done / 60)

    pages_number = len(pages_list)
    page_finished = "\t- {}/{} pages\n".format(pages_done, pages_number)
    minutes_finished = "\t- {}/{} minutes\n".format(minutes_done, minutes_total)
    result.append(page_finished)
    result.append(minutes_finished)
    pie_chart(
        data_dict={
            "finished": round(minutes_done / minutes_total * 100),
            "to be done": round((minutes_total - minutes_done) / minutes_total * 100)
        },
        chart_name="finish-percentage-{}".format(video_title)
    )
    img_finished = "\t- <img src=\"https://github.com/Yin-FR/Learning/blob/main/assets/finish-percentage-{}.png?raw=true\" alt=\"\" />\n".format(video_title.replace(" ", "%20"))
    result.append(img_finished)
    result.append("- Deatil:\n")

    for (idx, page) in enumerate(pages_list):
        page_duration = page["duration"]
        page_title = page["title"]
        page_link = page["link"]
        if idx not in finished:
            detail_text = "\t- [ ] [{}]({}) {}\n".format(page_title, page_link, page_duration[1])
        else:
            detail_text = "\t- [x] [{}]({}) {}\n".format(page_title, page_link, page_duration[1])
        result.append(detail_text)
    
    return result, minutes_done


def info_summary(info, video_title, finished=0) -> list:
    link = "https://github.com/Yin-FR/Learning/blob/main/learnings/{}.md".format(video_title.replace(" ", "%20"))
    duration = round(get_video_duration(info)[0] / 60)
    done = " " if finished < duration else "x"
    result = ["- [{}] [{}]({}) {}/{} minutes\n".format(done, video_title, link, finished, duration)]
    return result


async def add_record(bvid, basic_paths, subject, is_paged, finished, mark) -> None:
    result = await import_video(bvid)
    text_page, minutes_down = info_text(result, subject, is_paged, finished)
    insert_lines_markdown(basic_paths[1], "./learnings/{}.md".format(subject), text_page, "VIDEO")
    insert_lines_markdown(basic_paths[0], "./README.md", info_summary(result, subject, minutes_down), mark)