import shutil
from pathlib import Path
import tomli
import argparse
import sys

modPath = Path(__file__).parent.parent

target = {}
config = {}

"""
if not Path('config.toml').exists:
    shutil.copyfile(modPath / 'config.toml','config.toml')
with open('config.toml','rb') as conf:
    config = tomli.loads(conf)
#配置文件，先咕一会
"""

config['pandocArgs']=[
    '-f',
    'markdown-blank_before_header+lists_without_preceding_blankline',
    '--katex'
]

arg_parser = argparse.ArgumentParser(description='爬取洛谷题目并且进行格式转化')
arg_parser.add_argument('-p','--problem',action='append',help='题目列表')
arg_parser.add_argument('-t','--training',action='append',help='题单列表')
arg_parser.add_argument('--pandoc-args',type=str,help='传给pandoc的参数')

def parse_args():
    args = arg_parser.parse_args()
    args = {**vars(args)}
    target['problem'] = args['problem']
    target['training'] = args['training']
    if 'pandoc-args' in args:
        config['pandocArgs'] = args['pandoc-args']
