"""协程"""
import asyncio

try:
    import luogu
    import setting
except ModuleNotFoundError:
    from lgsv import luogu, setting

#if not Path("head.tex").exists:
#
#    shutil.copyfile(setting.modPath / "config" / "head.tex", "head.tex")


async def main():
    """main 函数"""
    setting.parse_args()
    md_src = ""
    problems = []
    trainings = []
    if ("problem" in setting.target) & (setting.target["problem"] is not None):
        for p in setting.target["problem"]:
            problems.append(luogu.Problem(problem_id=p, config=setting.golbal_config))
    if ("training" in setting.target) & (setting.target["training"] is not None):
        for t in setting.target["training"]:
            trainings.append(luogu.Training(training_id=t))
    async with asyncio.TaskGroup() as tg:
        for t in trainings:
            tg.create_task(t.fetch_resources())
    for t in trainings:
        problems.extend(t.get_problem_list())
    async with asyncio.TaskGroup() as tg:
        for p in problems:
            tg.create_task(p.fetch_resources())
    for p in problems:
        md_src += p.get_markdown(setting.golbal_config['order'])
    with open(file="out.md", mode="w",encoding="utf-8") as f:
        f.write(md_src)

def run():
    """运行 main 函数"""
    asyncio.run(main())

#    pypandoc.convert_text(md_src,format='md',to='pdf',extra_args=setting.config['pandocArgs'],outputfile="./out.pdf")

if __name__ == "__main__":
    run()
