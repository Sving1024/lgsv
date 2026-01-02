"""save module"""

import asyncio
import pathlib


from lgsv import log, setting

async def save_problems(
    problems,
    trainings,
    output_file=pathlib.Path("out.md"),
    order=None,
    problem_filter=None,
    language="zh-CN",
):
    """save problems to markdown file"""
    if order is None:
        order = setting.saver_config["order"]
    md_src = ""
    try:
        async with asyncio.TaskGroup() as tg:
            for t in trainings:
                tg.create_task(t.fetch_resources())
            for p in problems:
                tg.create_task(p.fetch_resources())
    except (ExceptionGroup, BaseExceptionGroup) as e:
        log.logger.error("无法获取某些题目的信息。其余任务已取消。")
        log.logger.error("%s", e)
        return
    if problem_filter is not None:
        problems = problem_filter.filt(problems)
    for p in problems:
        md_src += p.get_markdown(order, language)
    for t in trainings:
        md_src += t.get_markdown(order, language)
    with output_file.open(mode="w", encoding="utf-8") as f:
        f.write(md_src)
