from bilibili.import_func import get_video_pages, get_video_duration
from chart.piechart import pie_chart


def info_text(info, video_title, pages=False, finished=[-1]) -> list:
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
    for (idx, page) in enumerate(pages_list):
        if idx in finished:
            pages_done += 1
            minutes_done += round(page["duration"][0] / 60)

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
    img_finished = "\t- <img src=\"https://github.com/Yin-FR/Learning/blob/main/assets/finish-percentage-{}.png?raw=true\" alt=\"\" />\n".format(video_title)
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
    
    return result