# lgsv

LuoGu problem/training SaVer.

爬取洛谷题目。
尚未完工。

目前实现的功能：
- 爬取题单
- 将题目的 markdown 保存下来，存到当前目录的 out.md 中

使用 `-t` 或者 `--training` 指定题单。使用 `-p` 或者 `--problem` 指定题目。

使用 `--order=` 来指定放置 markdown 的顺序。
例如，要将按顺序保存题目背景，描述，输入格式，输出格式，使用 `--order=b,d,if,of`。

待办：
1. 编写pytest
2. 处理各类异常
3. 添加更多功能
4. 完善文档