import json

import httpx

headers = {
    "x-csrf-token": "",
}

params = {"_contentOnly": ""}

class Problem:
    __BASE_URL = "https://www.luogu.com.cn/problem/"
    problem_id = ""
    data = None
    markdown = ""
    config = None

    def __init__(self, problem_id, config) -> None:
        self.problem_id = problem_id
        self.config = config

    def part_markdown(self, part):
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
            return ret
        return ret + self.data[p] + "\n"

    async def fetch_resources(self) -> httpx.Response:
        # 将请求存储到 __html_cache 中
        print("从" + self.__BASE_URL + self.problem_id + "获取数据")
        async with httpx.AsyncClient() as client:
            raw_resources = await client.get(
                self.__BASE_URL + self.problem_id, params=params, headers=headers
            )
        print("解析题目" + self.problem_id)
        # 解析请求到的 json
        rescoures = json.loads(raw_resources.text)
        self.data = rescoures["currentData"]["problem"]
        self.markdown = self.part_markdown("title")
        for c in self.config["order"]:
            self.markdown += self.part_markdown(c)
        cnt_d = 0
        i = 0
        while i < len(self.markdown):
            if self.markdown[i] == "$":
                cnt_d += 1
                if (cnt_d & 1) == 1:
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
            i += 1
        return self.data

    def diffculty(self) -> int:
        return self.data["diffculty"]


class Training:
    __BASE_URL = "https://www.luogu.com.cn/training/"
    training_id = ""
    data = None
    problemList = []
    config = None

    def __init__(self, training_id, config) -> None:
        self.training_id = training_id
        self.config = config

    async def fetch_resources(self) -> httpx.Response:
        print("从" + self.__BASE_URL + self.training_id + "获取数据")
        async with httpx.AsyncClient() as client:
            raw_resources = await client.get(
                self.__BASE_URL + self.training_id, params=params, headers=headers
            )
        print("解析题单" + self.training_id)
        rescoures = json.loads(raw_resources.text)
        self.data = rescoures["currentData"]["training"]
        for p in self.data["problems"]:
            self.problemList.append(Problem(problem_id=p["problem"]["pid"], config=self.config))
        return self.data

    def get_problem_list(self):
        return self.problemList
