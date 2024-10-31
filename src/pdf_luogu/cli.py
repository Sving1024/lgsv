import pypandoc
from pathlib import Path
import asyncio
import shutil
try:
    import luogu, setting
except ModuleNotFoundError:
    from pdf_luogu import luogu, setting

if not Path('head.tex').exists:
    shutil.copyfile(setting.modPath / 'config' / 'head.tex','head.tex')

async def main():
    setting.parse_args()
    mdSrc = ''
    problems = []
    if ('problem' in setting.target) & (setting.target['problem']!=None):
        for p in setting.target['problem']:
            problems.append(luogu.Problem(p))
    if ('training' in setting.target) & (setting.target['training']!=None):
        for t in setting.target['training']:
            training = luogu.Training(t)
            await training.fetchResources()
            problems.extend(training.getProblemList())
    for p in problems:
        await p.fetchResources()
        mdSrc += p.markdown
    with open('out.md','w') as f:
        f.write(mdSrc)
#    pypandoc.convert_text(mdSrc,format='md',to='pdf',extra_args=setting.config['pandocArgs'],outputfile="./out.pdf")

if __name__ == '__main__':
    asyncio.run(main())