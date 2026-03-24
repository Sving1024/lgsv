"""
luogu class
"""

import asyncio
import json

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, wait_fixed, RetryCallState

from lgsv import log, setting


headers = {
    "Accept": "application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Referer": "https://www.luogu.com.cn/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Priority": "u=0, i",
    "x-lentille-request": "content-only",
}

params = {"_contentOnly": ""}

async def fetch_csrf_token():
    """获取csrf token"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url="https://www.luogu.com.cn",
            #            params=params,
            headers=headers,
            #            cookies=cookies,
        )
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("meta", attrs={"name": "csrf-token"})
    if csrf_token is None:
        log.logger.error("无法获取 csrf token，请检查 cookie 是否正确")
        return None
    headers["x-csrf-token"] = str(csrf_token.get("content"))
    return headers["x-csrf-token"]

def retry_stop(retry_state: RetryCallState):
    """获取题单资源时发生异常的日志记录"""
    if retry_state.attempt_number > setting.global_config["max_retry_times"]:
        return False
    return True

def problem_exception_logger():
    """获取题目资源时发生异常的日志记录"""

    def callback(retry_state: RetryCallState):
        error_message = "未知异常"
        if retry_state.outcome is not None:
            error_message = str(retry_state.outcome.exception())
        log.logger.warning(
            "获取题目 %s 资源时发生异常。异常信息：%s",
            retry_state.args[0].problem_id,
            error_message,
        )

    return callback


class Problem:
    """洛谷题目类"""

    __BASE_URL = "https://www.luogu.com.cn/problem/"

    def __init__(self, problem_id: str) -> None:
        self.problem_id = problem_id
        self.problem_id: str
        # data = None
        self.markdown: str
        self.difficulty: int
        self.tags: list
        self.limits = {"time": [], "memory": []}
        self.content: dict
        self.accepted: bool
        self.submitted: bool
        self.sample: list

    def part_markdown(self, part, language="zh-CN"):
        """单独获取题目的部分markdown,如题目背景,题目描述等"""
        ret = ""
        p = part
        match part:
            case "samples" | "s":
                ret = "## 输入输出样例"
                p = "samples"
            case "background" | "b":
                ret = "## 题目背景"
                p = "background"
            case "formatI" | "if":
                ret = "## 输入格式"
                p = "formatI"
            case "formatO" | "of":
                ret = "## 输出格式"
                p = "formatO"
            case "hint" | "h":
                ret = "## 说明/提示"
                p = "hint"
            case "name" | "n":
                ret = "# "
                p = "name"
            case "description" | "d":
                ret = "## 题目描述"
                p = "description"
            case "translation" | "tr":
                ret = "## 题目翻译"
                p = "translation"
        if p != "name":
            ret += "\n"
        if p == "samples":
            for i, sample in enumerate(self.sample):
                ret += (
                    f"### 输入 \\#{str(i+1)}\n"
                    f"```\n"
                    f"{sample[0]}\n"
                    f"```\n"
                    f"### 输出 \\#{str(i+1)}\n"
                    f"```\n"
                    f"{sample[1]}\n"
                    f"```\n"
                )
            return ret
        if (
            p not in self.content[language]
            or self.content[language][p] is None
            or self.content[language][p] == ""
        ):
            return ""
        return ret + self.content[language][p] + "\n"

    @retry(
        stop=retry_stop,
        wait=wait_fixed(5),
        reraise=True,
        before_sleep=problem_exception_logger(),
    )
    async def fetch_resources(self):
        """取回题目资源并将其存储到 self.data 中,返回 self.data"""
        log.logger.warning("从 %s%s 获取数据", self.__BASE_URL, self.problem_id)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.__BASE_URL + self.problem_id,
                params=params,
                headers=headers,
                follow_redirects=True,
            )
        response.raise_for_status()
        log.logger.warning("解析题目 %s", self.problem_id)
        # 解析请求到的 json
        rescoures = json.loads(response.text)
        data = rescoures["data"]["problem"]
        self.difficulty = data["difficulty"]
        if self.difficulty is None:
            self.difficulty = 0
        self.tags = data["tags"]
        self.limits = data["limits"]
        self.content = rescoures["data"]["translations"]
        self.sample = data["samples"]
        if "accepted" in data:
            self.accepted = data["accepted"]
        else:
            self.accepted = False
        if "submmited" in data:
            self.submitted = data["submmited"]
        else:
            self.submitted = False

    def get_markdown(self, order: list, language="zh-CN"):
        """以 order 的顺序获取题目的markdown"""
        if hasattr(self, "markdown"):
            return self.markdown
        self.markdown = self.part_markdown("name", language)
        for c in order:
            self.markdown += self.part_markdown(c, language)
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


class ProblemFilter:
    """filter of problems"""

    def __init__(
        self,
        difficulty=None,
        include_tags=None,
        exclude_tags=None,
        include_accepted: bool = False,
        include_submitted: bool = False,
    ) -> None:
        if difficulty is None:
            difficulty = [0, 1, 2, 3, 4, 5, 6, 7]
        if include_tags is None:
            include_tags = []
        if exclude_tags is None:
            exclude_tags = []
        self.difficulty = difficulty
        self.include_tags = include_tags
        self.exclude_tags = exclude_tags
        self.include_accepted = include_accepted
        self.include_submitted = include_submitted

    def match(self, p: Problem) -> bool:
        """check if problem p matches the filter"""
        log.logger.warning("正在检查题目 %s 是否符合过滤条件", p.problem_id)
        if p.difficulty not in self.difficulty:
            return False
        if self.exclude_tags and set(self.exclude_tags).intersection(set(p.tags)):
            return False
        if self.include_tags and not set(self.include_tags).intersection(set(p.tags)):
            return False
        if not self.include_accepted and p.accepted:
            return False
        if not self.include_submitted and p.submitted:
            return False
        return True

    def filt(self, problem_list: list) -> list:
        """filter training t and return the filtered training"""
        filtered_problems = []
        for p in problem_list:
            if self.match(p):
                filtered_problems.append(p)
        return filtered_problems


def training_retry_logger(task_name):
    """获取题单资源时发生异常的日志记录"""

    def callback(retry_state: RetryCallState):
        error_message = "未知异常"
        if retry_state.outcome is not None:
            error_message = str(retry_state.outcome.exception())
        log.logger.warning(
            "题单 %s 进行任务 %s 时失败。异常信息：%s",
            task_name,
            retry_state.args[0].training_id,
            error_message,
        )

    return callback


class Training:
    """洛谷题单类"""

    __BASE_URL = "https://www.luogu.com.cn/training/"

    def __init__(self, training_id: str) -> None:
        self.training_id = training_id
        self.problem_list: list[Problem] = []
        self.markdown: str
        self.error_problems: list[str] = []
        self._fetch_cache_traning = None
        self._fetch_cache_traning_problem = None

    def handle_problem_exception(self, e, problem_id):
        """处理获取题目资源时的异常，根据设置决定是继续执行还是抛出异常"""
        if setting.global_config["ignore_error"]:
            log.logger.error(
                "获取题目 %s 信息失败：无法访问目标 url：%s", problem_id, e
            )
            self.error_problems.append(problem_id)
            self.problem_list = [p for p in self.problem_list if p.problem_id != problem_id]
        else:
            raise e

    @retry(
        stop=retry_stop,
        wait=wait_fixed(5),
        before_sleep=training_retry_logger("获取题单资源"),
        reraise=True,
    )
    async def fetch_training_resources(self):
        """取回题目资源并将其存储到 self.data 中,返回 self.data"""
        log.logger.warning("从 %s%s 获取数据", self.__BASE_URL, self.training_id)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.__BASE_URL + self.training_id,
                params=params,
                headers=headers,
                follow_redirects=True,
            )
        response.raise_for_status()
        log.logger.warning("解析题单 %s", self.training_id)
        rescoures = json.loads(response.text)
        data = rescoures["currentData"]["training"]
        for p in data["problems"]:
            self.problem_list.append(Problem(problem_id=p["problem"]["pid"]))

    async def fetch_problem(self, p:Problem):
        """取回题单中所有题目的资源"""
        try:
            await p.fetch_resources()
        except httpx.HTTPStatusError as e:
            self.handle_problem_exception(e, p.problem_id)

    @retry(
        stop=retry_stop,
        wait=wait_fixed(5),
        before_sleep=training_retry_logger("获取题单中题目的资源"),
        reraise=True,
    )
    async def fetch_problem_resources(self):
        """取回题单中所有题目的资源"""
        async with asyncio.TaskGroup() as tg:
            for p in self.problem_list:
                tg.create_task(self.fetch_problem(p))

    async def fetch_resources(self):
        """取回题单中所有题目的资源"""
        if self._fetch_cache_traning is None:
            self._fetch_cache_traning = asyncio.create_task(self.fetch_training_resources())
        await self._fetch_cache_traning
        if self._fetch_cache_traning_problem is None:
            self._fetch_cache_traning_problem = asyncio.create_task(self.fetch_problem_resources())
        await self._fetch_cache_traning_problem

    def remove_duplicates(self):
        """移除题单中重复的题目"""
        seen = set()
        unique_problems = []
        for p in self.problem_list:
            if p.problem_id not in seen:
                seen.add(p.problem_id)
                unique_problems.append(p)
        self.problem_list = unique_problems

    def get_markdown(self, order: list, language="zh-CN"):
        """获取题单中所有题目的 markdown"""
        self.markdown = ""
        for p in self.problem_list:
            self.markdown += p.get_markdown(order, language)
        return self.markdown

    def __len__(self):
        return len(self.problem_list)

    def add_problem(self, problem: Problem):
        """向题单中添加题目"""
        self.problem_list.append(problem)
        self.remove_duplicates()

    async def add_problem_with_id(self, problem_id: str):
        """向题单中添加题目"""
        p = Problem(problem_id=problem_id)
        self.problem_list.append(p)
        self.remove_duplicates()

    def merge_training(self, training: "Training"):
        """将另一个题单的题目合并到当前题单中"""
        for p in training.problem_list:
            self.problem_list.append(p)
        self.remove_duplicates()

    def remove_problem(self, problem_id):
        """从题单中移除题目"""
        self.problem_list = [p for p in self.problem_list if p.problem_id != problem_id]
        self.remove_duplicates()

    @retry(
        stop=retry_stop,
        wait=wait_fixed(5),
        before_sleep=training_retry_logger("提交更改"),
        reraise=True,
    )
    async def submit_changes(self):
        """同步题单与远程题单"""
        await fetch_csrf_token()
        await self.fetch_resources()
        self.remove_duplicates()
        log.logger.warning("同步题单 %s 与远程题单", self.training_id)
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=f"https://www.luogu.com.cn/api/training/editProblems/{self.training_id}",
                headers=headers,
                json={"pids": [p.problem_id for p in self.problem_list]},
                follow_redirects=True,
            )
        response.raise_for_status()

    async def filt_by(self, problem_filter: ProblemFilter):
        """使用 filter 过滤题单中的题目"""
        await self.fetch_resources()
        self.problem_list = problem_filter.filt(self.problem_list)
