# -*- coding: UTF-8 -*-

# Filename : dragon_ball.py
# author by : WeiQi

from urllib.parse import urljoin
import urllib.request

from bs4 import BeautifulSoup

import os
import datetime
import re
import errno

def mkdir_p(path):  # 递归创建多级目录
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def get_link(page):  # 寻找链接的href
    linkData = []
    for page in page.find_all('td'):
        links = page.select("a")
        for each in links:
            # if str(each.get('href'))[:1] == '/': 过滤if代码
            data = each.get('href')
            linkData.append(data)
    return (linkData)

def gain(url):  # 获取网页指定内容
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')  # 利用soup获取网页内容
    links = get_link(soup)  # 获取<a href= ? 内容
    return links

def getTideForecast(country):
    url = 'https://www.tide-forecast.com/countries/'+country
    Web_Link = gain(url)
    for Link in range(len(Web_Link)):
        Link_Add = Web_Link[Link]
        Link_One = re.split("/", Link_Add)  # 去除'/'，将Link_Add变成数组
        Link_Address = Link_One[2]  # 获取数组第3位值
        Link_Address = (Link_Address + '.js')
        url_Tide = 'https://www.tide-forecast.com/tides/'
        connet = urljoin(url_Tide, Link_Address)  # 拼接网址路径
        file = os.path.join('./TideData/'+ country + "/")  # 拼接绝对路径
        mkdir_p(file)
        print(connet)
        if os.path.isfile(file):
            print('文件已存在')
        else:
            try:
                start = datetime.datetime.now().replace(microsecond=0)  # 计时工具
                url = connet
                wp = urllib.request.urlopen(url)  # 打开数据网页数据
                content = wp.read()
                fp = open(file + Link_Address, "wb")  # 写入指定文件夹
                fp.write(content)  # 写入数据
                fp.close()  # 关闭文件
                end = datetime.datetime.now().replace(microsecond=0)
                print("用时: ", end='')
                print(end - start)
            except Exception as err:
                print(err)
            #finally:
            #    print("Goodbye!")

def getDragonBall():
    url = 'http://comic.dragonballcn.com/list/0.Dragon_Ball-buyao_daolian_ya/1.jp_original/01/DB01*.jpg'
    Web_Link = gain(url)
    for Link in range(len(Web_Link)):
        Link_Add = Web_Link[Link]
        Link_One = re.split("/", Link_Add)  # 去除'/'，将Link_Add变成数组
        Link_Address = Link_One[2]  # 获取数组第3位值
        Link_Address = (Link_Address + '.jpg')
        url_dragon = 'http://comic.dragonballcn.com/list/0.Dragon_Ball-buyao_daolian_ya/1.jp_original/01/'
        connet = urljoin(url_dragon, Link_Address)  # 拼接网址路径
        file = os.path.join('./DragonBall/Japan' + "/")  # 拼接绝对路径
        mkdir_p(file)
        print(connet)
        if os.path.isfile(file):
            print('文件已存在')
        else:
            start = datetime.datetime.now().replace(microsecond=0)  # 计时工具
            url = connet
            wp = urllib.request.urlopen(url)  # 打开数据网页数据
            content = wp.read()
            fp = open(file + Link_Address, "wb")  # 写入指定文件夹
            fp.write(content)  # 写入数据
            fp.close()  # 关闭文件
            end = datetime.datetime.now().replace(microsecond=0)
            print("用时: ", end='')
            print(end - start)

def getCountry(url):
    print()

if __name__ == '__main__':
    country = ['Cuba', 'China', 'Japan', 'Singapore', 'Bahrain', 'Kuwait', 'South Korea', 'Bangladesh', 'Malaysia', 'Sri Lanka']
    for str in country:
        getTideForecast(str)
    # getDragonBall()
