"""协程"""

import asyncio
import pathlib

from lgsv import log, luogu, setting, save, edit


async def main():
    """main 函数"""
    setting.parse_args()
    problem_filter = luogu.ProblemFilter(
        include_accepted=not setting.filter_config["exclude_finished"],
        exclude_tags=setting.filter_config["exclude_tag"],
        include_tags=setting.filter_config["include_tag"],
    )
    if setting.global_config["cookie"] is not None:
        luogu.headers["Cookie"] = setting.global_config["cookie"]
    match setting.global_config["action"]:
        case "save":
            await save.save_problems(
                problems=[luogu.Problem(p) for p in setting.saver_config["problem"]],
                trainings=[luogu.Training(t) for t in setting.saver_config["training"]],
                output_file=pathlib.Path(setting.saver_config["output"]),
                order=setting.saver_config["order"],
                problem_filter=problem_filter,
                language=setting.saver_config["language"],
            )
        case "edit":
            await edit.edit_training(
                training=luogu.Training(
                    training_id=setting.editor_config["training_id"]
                ),
                add_problem=[
                    luogu.Problem(p) for p in setting.editor_config["add_problem"]
                ],
                merge_training=[
                    luogu.Training(training_id=t)
                    for t in setting.editor_config["merge_training"]
                ],
                remove_problem=[
                    luogu.Problem(p) for p in setting.editor_config["remove_problem"]
                ],
                problem_filter=problem_filter,
            )
        case _:
            log.logger.error("不支持的操作：%s", setting.global_config["action"])


def run():
    """运行 main 函数"""
    asyncio.run(main())


if __name__ == "__main__":
    run()
