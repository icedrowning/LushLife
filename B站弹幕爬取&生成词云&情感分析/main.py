#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
import re
import json
#多p
url="https://www.bilibili.com/video/BV1fx411N7bU"
#单p
#url='https://www.bilibili.com/video/BV1ws411B7ix'

r = requests.get(url)
#先用bs4是因为这里正则会有多个匹配项，先过滤到只剩一个再用正则提取
soup = bs(r.text,"html.parser")

#这两个目前是相同的，但不清楚这两个结构实际会不会经常变动
#后续如果有时间需要看一下这里会不会有问题
# print(soup.head.contents[-3])
# print(soup.head.find_all('script')[-1])
raw_str=str(soup.head.find_all('script')[-1])

res = re.search(r'window\.__INITIAL_STATE__=({.*});',raw_str).group(1)
data=json.loads(res)

#data.keys() 里面好多key，目前用到的只有videoData中的pages
#目前看来如果弹幕视频分p，则会有part用于存储p名；如果是单p则字典不会有这个key
#后续需要分情况

for i in data['videoData']['pages']:
    print(str(i['cid'])+i['part'])

#part要存歌名，后面用

##################

print(111111111)
r_comment = requests.get("https://comment.bilibili.com/2165695.xml")
#bs4again


soup_comment = bs(r_comment.content.decode(encoding='UTF-8'),"html.parser")
print(soup_comment.contents[1])
#明天继续
