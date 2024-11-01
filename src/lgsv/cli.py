import asyncio
import shutil
from pathlib import Path

try:
    import luogu
    import setting
except ModuleNotFoundError:
    from lgsv import luogu, setting

if not Path("head.tex").exists:
    shutil.copyfile(setting.modPath / "config" / "head.tex", "head.tex")


async def main():
    setting.parse_args()
    md_src = ""
    problems = []
    if ("problem" in setting.target) & (setting.target["problem"] is not None):
        for p in setting.target["problem"]:
            problems.append(luogu.Problem(problem_id=p, config=setting.golbal_config))
    if ("training" in setting.target) & (setting.target["training"] is not None):
        for t in setting.target["training"]:
            training = luogu.Training(training_id=t, config=setting.golbal_config)
            await training.fetch_resources()
            problems.extend(training.get_problem_list())
    for p in problems:
        await p.fetch_resources()
        md_src += p.markdown
    with open("out.md", "w") as f:
        f.write(md_src)


#    pypandoc.convert_text(md_src,format='md',to='pdf',extra_args=setting.config['pandocArgs'],outputfile="./out.pdf")

if __name__ == "__main__":
    asyncio.run(main())
