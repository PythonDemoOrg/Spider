# -*- coding: UTF-8 -*-

# Filename : block_chain.py
# author by : WeiQi

import json

class SimpleCrawler:
    init_url = "https://zhuanlan.zhihu.com/api/columns/SVlaw/followers"
    offset = 0

    def crawl(self, params=None):
        import requests
        # 必须指定UA，否则知乎服务器会判定请求不合法
        headers = {
            "Host": "zhuanlan.zhihu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        response = requests.get(self.init_url, headers=headers, params=params)
        print(response.url)
        data = response.json()
        # 分页加载更多，递归调用 这里为了演示只获取前100条数据
        while self.offset < 100:
            self.parse(data)
            self.offset += 20
            params = {"limit": 20, "offset": self.offset}
            self.crawl(params)

    def parse(self, data):
        # 以json格式存储到文件
        with open("followers.json", "a", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item))
                f.write('\n')


if __name__ == '__main__':
    SimpleCrawler().crawl()