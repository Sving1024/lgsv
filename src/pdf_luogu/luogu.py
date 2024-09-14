"""json解析"""
import json

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
    __html_cache=None

    def __init__(self,_id) -> None:
        self.id=_id

    def fetchResources(self) -> httpx.Response :
        """将请求存储到 __html_cache 中"""
        self.__html_cache=httpx.get(self.__BASE_URL+self.id,params={'_contentOnly' : ''})
        return self.__html_cache
    def parseRespose(self):
        """解析请求到的 json"""
        tmp=json.loads(self.__html_cache.text)
        self.data = tmp['currentData']['problem']
        return self.data


class Training:
    __BASE_URL='https://www.luogu.com.cn/training/'
    id=''
    data=None
    __html_cache=None

    def __init__(self,_id) -> None:
        self.id=_id

    def fetchResources(self) -> httpx.Response:
        if self.__html_cache != None:
            return self.__html_cache
        self.__html_cache=httpx.get(self.__BASE_URL+self.id,params={'_contentOnly' : ''})
        return self.__html_cache

    def parseRespose(self):
        tmp = json.loads(self.__html_cache.text)
        self.data=tmp['currentData']['training']
        return self.data
