"""
json 解析获取的 json
httpx 用于发送 http 请求
BeautifulSoup 解析html
"""

import json

import httpx
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Referer": "https://www.luogu.com.cn/",
    "Connection": "keep-alive",
    #    "Cookie": "",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0, i",
    #    "x-csrf-token": "",
}
params = {"_contentOnly": ""}

"""
async def fetch_csrf_token():
    获取csrf token
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://www.luogu.com.cn",
            #            params=params,
            headers=headers,
#            cookies=cookies,
        )
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("meta", attrs={"name": "csrf-token"})
    headers["x-csrf-token"] = csrf_token.get("content")
    return headers["x-csrf-token"]
"""


class Problem:
    """洛谷题目类"""

    __BASE_URL = "https://www.luogu.com.cn/problem/"
    problem_id = ""
    data = None
    markdown = ""

    def __init__(self, problem_id) -> None:
        self.problem_id = problem_id

    def part_markdown(self, part):
        """单独获取题目的部分markdown,如题目背景,题目描述等"""
        ret = None
        p = part
        match part:
            case "samples" | "s":
                ret = "## 输入输出样例"
                p = "samples"
            case "background" | "b":
                ret = "## 题目背景"
                p = "background"
            case "inputFormat" | "if":
                ret = "## 输入格式"
                p = "inputFormat"
            case "outputFormat" | "of":
                ret = "## 输出格式"
                p = "outputFormat"
            case "hint" | "h":
                ret = "## 说明/提示"
                p = "hint"
            case "title" | "ti":
                ret = "# "
                p = "title"
            case "description" | "d":
                ret = "## 题目描述"
                p = "description"
            case "translation" | "tr":
                ret = "## 题目翻译"
                p = "translation"
        if str(p) not in self.data or self.data[p] is None:
            return ""
        if p != "title":
            ret += "\n"
        if p == "samples":
            ret = "#"
            i = 1
            for sample in self.data[p]:
                ret += (
                    "### 输入 \\#"
                    + str(i)
                    + "\n```\n"
                    + sample[0]
                    + "\n```\n### 输出 \\#"
                    + str(i)
                    + "\n```\n"
                    + sample[1]
                    + "\n```\n"
                )
                i += 1
            return ret
        return ret + self.data[p] + "\n"

    async def fetch_resources(self):
        """取回题目资源并将其存储到 self.data 中,返回 self.data"""
        # 将请求存储到 __html_cache 中
        print("从" + self.__BASE_URL + self.problem_id + "获取数据")
        async with httpx.AsyncClient() as client:
            raw_resources = await client.get(
                self.__BASE_URL + self.problem_id,
                params=params,
                headers=headers,
                #                cookies=cookies,
            )
        print("解析题目" + self.problem_id)
        # 解析请求到的 json
        rescoures = json.loads(raw_resources.text)
        self.data = rescoures["currentData"]["problem"]
        return self.data

    def get_markdown(self, order=None):
        """以 order 的顺序获取题目的markdown"""
        if order is None:
            order = ["b", "d", "if", "of", "s", "h", "tr"]
        self.markdown = self.part_markdown("title")
        for c in order:
            self.markdown += self.part_markdown(c)
        cnt_d = 0
        i = 0
        while i < len(self.markdown):
            if self.markdown[i] == "$":
                cnt_d += 1

                if (cnt_d & 1) == 1:
                    if self.markdown[i + 1] == "$":
                        i += 1
                    nxt_c = i + 1
                    while self.markdown[nxt_c] == " ":
                        nxt_c += 1
                    self.markdown = (
                        self.markdown[: i + 1]
                        + self.markdown[-(len(self.markdown) - nxt_c) :]
                    )
                else:
                    prev_c = i - 1
                    while self.markdown[prev_c] == " ":
                        prev_c -= 1
                    self.markdown = (
                        self.markdown[: prev_c + 1]
                        + self.markdown[-(len(self.markdown) - i) :]
                    )
                    i = prev_c + 1
                    if self.markdown[i + 1] == "$":
                        i += 1
            i += 1
        return self.markdown

    def diffculty(self) -> int:
        """返回题目难度"""
        return self.data["diffculty"]


class Training:
    """洛谷题单类"""

    __BASE_URL = "https://www.luogu.com.cn/training/"
    training_id = ""
    data = None
    problemList = []

    def __init__(self, training_id) -> None:
        self.training_id = training_id

    async def fetch_resources(self):
        """取回题目资源并将其存储到 self.data 中,返回 self.data"""
        print("从" + self.__BASE_URL + self.training_id + "获取数据")
        async with httpx.AsyncClient() as client:
            raw_resources = await client.get(
                self.__BASE_URL + self.training_id,
                params=params,
                headers=headers,
                #                cookies=cookies,
            )
        print("解析题单" + self.training_id)
        rescoures = json.loads(raw_resources.text)
        self.data = rescoures["currentData"]["training"]
        for p in self.data["problems"]:
            self.problemList.append(Problem(problem_id=p["problem"]["pid"]))
        return self.data

    def get_problem_list(self):
        """返回题单包含的题目列表"""
        return self.problemList
