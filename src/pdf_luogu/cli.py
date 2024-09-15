import pypandoc
from pathlib import Path
import shutil
import sys
#ys.path.append('')
#sys.path.append('../')
try:
    import luogu, setting
except ModuleNotFoundError:
    from pdf_luogu import luogu, setting

if not Path('head.tex').exists:
    shutil.copyfile(setting.modPath / 'config' / 'head.tex','head.tex')

def main():
    setting.parse_args()
    mdSrc = ''
    problems = []
    for p in setting.target['problem']:
        problems.append(luogu.Problem(p))
    for t in setting.target['training']:
        training = luogu.Training(t)
        training.fetchResources()
        problems.extend(training.getProblemList())
    for p in problems:
        p.fetchResources()
        mdSrc += p.markdown
    pypandoc.convert_text(mdSrc,format='md',to='pdf',extra_args=setting.config['pandocArgs'],outputfile="./out.pdf")

if __name__ == '__main__':
    main()