# -*- coding: UTF-8 -*-

# Filename : get_photo.py
# author by : WeiQi

import urllib.request
import urllib
import re
import os
import socket

def get_html(url):
    socket.setdefaulttimeout(2)
    papg = urllib.request.urlopen(url)
    html = papg.read()
    # html = unicode(html, "gbk").encode("utf8")
    return html

def get_img(html):
    imgre = re.compile(r'<img src="(.*?)"')
    imglist = re.findall(imgre, html)
    for imgurl in imglist:
        print ("imgurl"+imgurl)
        global x
        urllib.urlretrieve(imgurl, '.\\photo\%05d.jpg'%x)
        x += 1
        print("正在下载第%s张图片"%x)

def get_tag_list(html):
    szurlre = re.compile(r'<a href="(http://www.5442.com/tag/.*?.html)" class')
    tag_list = re.findall(szurlre, html)
    return tag_list

def get_page_num(html):
    html = html.decode('gbk')
    szurlre = re.compile(r'(\d+).html\'>末页')
    szresult = re.findall(szurlre, html)
    if len(szresult) == 0:
        page_num = 0
    else:
        page_num = int(szresult[0])
    print (page_num)
    return page_num

def get_page_num2(html):
    html = html.decode('gbk')
    szurlre = re.compile(r'共(\d+)页')
    szresult = re.findall(szurlre, html)
    if len(szresult) == 0:
        page_num = 0
    else:
        page_num = int(szresult[0])
    return page_num

#获得单页的相册
def get_ablum_list(html):
    html = html.decode('gbk')
    szurlre = re.compile(r'(http://www.5442.com/meinv/2\d+/\d+.html)" target=')
    ablum_list = re.findall(szurlre, html);
    return ablum_list

#获得相册的名称
def get_ablum_name(html):
    szurlre = re.compile(r'<title>(\S+)</title>')
    ablum_name = re.findall(szurlre, html)
    return ablum_name[0]

#获得单页的图片
def get_photo(html, dir, photo_num):
    html = html.decode('gbk')
    imgre = re.compile(r'点击图片进入下一页\' ><img src=\'(http://\S+.jpg)\' alt=')
    imglist = re.findall(imgre, html)
    for imgurl in imglist:
        try:
            socket.setdefaulttimeout(2)
            urllib.urlretrieve(imgurl, './photo//%s//%05d.jpg'%(dir, photo_num))
            print("正在下载第%s张图片"%photo_num)
            photo_num = photo_num + 1
        except:
            continue
    return photo_num

url = "http://www.5442.com/meinv/"
baseurl = "http://www.5442.com"
html = get_html(url)
page_num = get_page_num(html)
print ("一共有%s页"%page_num)
ablum_num = 0
try:
    os.mkdir("./photo")
except:
    print ("目录已经存在")
for i in range(1, page_num):
    if i != 1:
        url = "http://www.5442.com/meinv/list_1_%s.html"%i
        try:
            html = get_html(url)
        except:
            continue
    ablum_list = get_ablum_list(html)
    for ablum_url in ablum_list:
        ablum_num = ablum_num + 1
        try:
            photo_html = get_html(ablum_url)
        except:
            continue
        url_part = ablum_url[0:-5]
        photo_page_num = get_page_num2(photo_html)
        print("photo_page_num=%d"%photo_page_num)
        ablum_name = "编程资料" + "%05d" % ablum_num
        print ("ablum_name: "+ablum_name)
        photo_num = 0
        #创建相册对应的目录
        ui_ablum_name = ablum_name
        try:
            os.mkdir("./photo/"+ui_ablum_name)
        except:
            continue
        for i in range(1, photo_page_num):
            if i != 1:
                ablum_url = url_part + "_%d"%i + ".html"
                try:
                  photo_html = get_html(ablum_url)
                except:
                  continue
            photo_num = get_photo(photo_html, ablum_name, photo_num)