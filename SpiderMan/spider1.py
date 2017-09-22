#coding=utf-8
__author__ = 'York'

import re

import urllib

import urllib.request
import urllib.response
page = 1

url = 'https://www.qiushibaike.com/hot/page/'+str(page)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = {'User-Agent':user_agent}

try:
    request = urllib.request.Request(url,headers=headers)
    #request.add_header()
    response = urllib.request.urlopen(request)
    #content = urllib.request.urlopen(request).read().decode('utf-8')

except urllib.request.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)

content = response.read().decode('utf-8')


pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>(.*?)stats-vote.*?<i class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)


def del_list(list,num):
    del list[num]
    return list

items = [del_list(list(item),2)  for item in items if item[2].find('<img src=')==-1]

for i,v in enumerate(items):
    print(i,v)










# def filter(item):
#     temp = [x for x in item if item[2].find('<img src=') == -1]
#     del temp[2]
#     return temp
#
#
#
#
# filter_items = list(map(filter,items))
#
#








# for item in items:
#     print( item[0],item[1],item[2],item[3],item[4])

# content = urllib.response.read().decode('utf-8')
# pattern = re.compile('<div.*?author\s{1}clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
# items = re.findall(pattern,content)
# for item in items:
#     print( item[0],item[1],item[2],item[3],item[4])

