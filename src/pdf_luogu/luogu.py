"""json解析"""
import json
import config
import httpx


class Problem:
    """
    洛谷题目类
    id 题目编号
    __html_cache html缓存
    data 用于存储题目的数据，从请求到的json中解析出来的
    """
    __BASE_URL='https://www.luogu.com.cn/problem/'
    id=''
    data=None
    markdown = ''

    def __init__(self,_id) -> None:
        self.id=_id

    def partMarkdown(self,part):
        ret = None
        match part:
            case 'samples':
                ret = '## 输入输出样例'
            case 'background':
                ret = '## 题目背景'
            case 'inputFormat':
                ret = '## 输入格式'
            case 'outputFormat':
                ret = '## 输出格式'
            case 'hint':
                ret = '##说明/提示'
            case 'title':
                ret = '# '
            case 'description':
                ret = '## 题目描述'
        if part != 'title':
            ret += '\n'
        if part == 'samples':
            ret = '#'
            i = 1
            for sample in self.data[part]:
                ret += '### 输入 \\#'+str(i)+'\n```\n'+sample[0]+'```\n### 输出 \\#'+str(i)+'\n```\n'+sample[1]+'```\n'
            return ret
        return ret + self.data[part] + '\n'

    def fetchResources(self) -> httpx.Response :
        """将请求存储到 __html_cache 中"""
        raw_resources=httpx.get(self.__BASE_URL+self.id,params={'_contentOnly' : ''})
        """解析请求到的 json"""
        rescoures=json.loads(raw_resources.text)
        self.data = rescoures['currentData']['problem']
        self.markdown=(
            self.partMarkdown('title') +
            self.partMarkdown('description') +
            self.partMarkdown('inputFormat') +
            self.partMarkdown('outputFormat') +
            self.partMarkdown('samples') +
            self.partMarkdown('hint')
        )
        return self.data

    def diffculty(self) -> int:
        return self.data['diffculty']

class Training:
    __BASE_URL='https://www.luogu.com.cn/training/'
    id=''
    data=None
    problemList = []

    def __init__(self,_id) -> None:
        self.id=_id

    def fetchResources(self) -> httpx.Response:
        raw_resources=httpx.get(self.__BASE_URL+self.id,params={'_contentOnly' : ''})
        rescoures = json.loads(raw_resources.text)
        self.data=rescoures['currentData']['training']
        for p in self.data['problems']:
            self.problemList.append(Problem(p['problem']['pid']))
        return self.data
    
    def getProblemList(self):
        return self.problemList


x = Problem('P1001')
x.fetchResources()

with open("/home/Sving1024/test.md","w") as f:
    f.write(x.markdown)