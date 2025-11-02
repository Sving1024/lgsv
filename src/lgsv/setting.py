"""
config
"""

import argparse

# modPath = Path(__file__).parent.parent

saver_config = {
    "problem": [],
    "training": [],
    "order": ["b", "d", "if", "of", "s", "h", "tr"],
    "output": "out.md",
}

editor_config = {
    "training_id": "",
    "add_problem": [],
    "merge_training": [],
    "remove_problem": [],
}

global_config = {
    "cookie": "",
    "max_retry_times": 5,
    "loglevel": "WARNING",
}

filter_config = {
    "exclude_finished": False,
    "exclude_submitted": False,
    "exclude_tag": [],
    "include_tag": [],
}

arg_parser = argparse.ArgumentParser(
    description="爬取洛谷题目并且进行格式转化",
    formatter_class=argparse.RawTextHelpFormatter,
)


def init_arg_parser():
    """初始化参数解析器"""
    action_parser = arg_parser.add_subparsers(title="action", dest="action")
    save_options = action_parser.add_parser("save", help="保存题目为 markdown")

    save_options.description = "save 相关选项"
    save_options.add_argument("-p", "--problem", action="append", help="题目列表")
    save_options.add_argument("-t", "--training", action="append", help="题单列表")
    save_options.add_argument("-o", "--output", type=str, help="输出 markdown 的位置")
    save_options.add_argument(
        "--order",
        type=str,
        help="\n".join(
            [
                "指定题目部分的顺序，用逗号分隔。",
                "b/background 对应题目背景",
                "s/samples 对应样例",
                "if/inputFormat 对应输入格式",
                "of/outputFormat 对应输出格式",
                "h/hint 对应说明/提示",
                "d/description 对应题目描述",
                "tr/translation 对应题目翻译。",
            ]
        ),
    )

    edit_options = action_parser.add_parser("edit", help="编辑题单")
    edit_options.description = "edit 相关选项"
    edit_options.add_argument("training_id", type=str, help="题单 ID")
    edit_options.add_argument("--add-problem", action="append", help="添加题目到题单")
    edit_options.add_argument("--merge-training", action="append", help="合并题单")
    edit_options.add_argument(
        "--remove-problem", action="append", help="从题单中删除题目"
    )

    filter_options = arg_parser.add_argument_group("过滤选项")
    filter_options.description = "用于过滤题目"
    filter_options.add_argument("--exclude-finished", action="store_true", help="排除已完成题目")
    filter_options.add_argument(
        "--exclude-tag", action="append", help="排除指定标签的题目"
    )
    filter_options.add_argument(
        "--include-tag", action="append", help="保留指定标签的题目"
    )

    arg_parser.add_argument("-c", "--cookie", type=str, help="洛谷cookie")
    arg_parser.add_argument("--loglevel", type=str, help="日志等级")
    arg_parser.add_argument("--max-retry-times", type=int, help="失败时重试次数")
    


def parse_filter_args(args):
    """处理过滤参数"""
    if args.exclude_finished is not None:
        filter_config["exclude_finished"] = args.exclude_finished
    if args.exclude_tag is not None:
        filter_config["exclude_tag"] = args.exclude_tag
    if args.include_tag is not None:
        filter_config["include_tag"] = args.include_tag


def parse_edit_args(args):
    """处理编辑参数"""
    editor_config["training_id"] = args.training_id
    editor_config["add_problem"] = args.add_problem
    if args.add_problem is None:
        editor_config["add_problem"] = []
    editor_config["merge_training"] = args.merge_training
    if args.merge_training is None:
        editor_config["merge_training"] = []
    editor_config["remove_problem"] = args.remove_problem
    if args.remove_problem is None:
        editor_config["remove_problem"] = []


def parse_save_args(args):
    """处理保存参数"""
    saver_config["problem"] = args.problem
    if saver_config["problem"] is None:
        saver_config["problem"] = []
    saver_config["training"] = args.training
    if saver_config["training"] is None:
        saver_config["training"] = []
    if args.output is not None:
        saver_config["output"] = args.output
    if args.order is not None:
        order_map = {
            "b": "b",
            "background": "b",
            "s": "s",
            "samples": "s",
            "if": "if",
            "inputFormat": "if",
            "of": "of",
            "outputFormat": "of",
            "h": "h",
            "hint": "h",
            "d": "d",
            "description": "d",
            "tr": "tr",
            "translation": "tr",
        }
        order_list = args["order"].split(",")
        parsed_order = []
        for item in order_list:
            if item in order_map:
                parsed_order.append(order_map[item])
        if len(parsed_order) > 0:
            saver_config["order"] = parsed_order


def parse_args():
    """处理参数"""
    init_arg_parser()
    args = arg_parser.parse_args()

    if args.max_retry_times is not None:
        global_config["max_retry_times"] = args.max_retry_times
    if args.loglevel is not None:
        global_config["loglevel"] = args.loglevel

    if "cookie" in args:
        global_config["cookie"] = args.cookie

    global_config["action"] = args.action
    match args.action:
        case "save":
            parse_save_args(args)
        case "edit":
            parse_edit_args(args)
        case _:
            pass

    parse_filter_args(args)

    return args
