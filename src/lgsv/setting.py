"""
argparse 处理命令行参数
"""

import argparse

# modPath = Path(__file__).parent.parent

target = {}
global_config = {"order": None}

cookies = {
    "__client_id": "",
    "_uid": "",
}

"""
if not Path('config.toml').exists:
    shutil.copyfile(modPath / 'config.toml','config.toml')
with open('config.toml','rb') as conf:
    config = tomli.loads(conf)
#配置文件，先咕一会
"""

global_config["pandocArgs"] = [
    "-f",
    "markdown-blank_before_header+lists_without_preceding_blankline",
    "--katex",
    "--pdf-engine=xelatex",
    "-V mainfont='等线'",
    #    '--include-in-header=head.tex',
]

arg_parser = argparse.ArgumentParser(description="爬取洛谷题目并且进行格式转化")
arg_parser.add_argument("-p", "--problem", action="append", help="题目列表")
arg_parser.add_argument("-t", "--training", action="append", help="题单列表")
arg_parser.add_argument("--pandoc-args", type=str, help="传给pandoc的参数")
# arg_parser.add_argument("--client-id", type=str, help="client id")
arg_parser.add_argument("--order", type=str, help="指定题目部分的顺序")
# arg_parser.add_argument("-u","--uid",type=int,help="洛谷uid")
arg_parser.add_argument("-c", "--cookie", type=str, help="洛谷cookie")


def parse_args():
    """处理参数"""
    args = arg_parser.parse_args()
    args = {**vars(args)}
    target["problem"] = args["problem"]
    target["training"] = args["training"]
    if "pandoc_args" in args:
        global_config["pandocArgs"] = args["pandoc_args"]
    if "cookie" in args:
        global_config["cookie"] = args["cookie"]

    #    if "uid" in args:
    #        global_config["uid"] = args["uid"]
    #        cookies["_uid"]=args["uid"]
    if "order" in args:
        global_config["order"] = args["order"].split(",")


#    if "client_id" in args:
#        global_config["client_id"]=args["client_id"]
#        cookies["__client_id"]=args["client_id"]
