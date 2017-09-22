#coding=utf-8
__author__ = 'York'

import re

import urllib

import urllib.request
import urllib.response
import urllib.parse
page = 1
url = 'http://dailianmao.com/prizeFix.action'

duanwei = ['青铜3','青铜2','青铜1','白银3','白银2','白银1','黄金4','黄金3','黄金2','黄金1',
          '铂金4','铂金3','铂金2','铂金1','钻石5','钻石4','钻石3','钻石2','钻石1','星耀5',
          '星耀4','星耀3','星耀2','星耀1']

import time

#print(int(time.time()*1000))

parameters = [
    ('areaname' , '安卓-微信'),
    ('begingrade' , duanwei[0]),
    ('beginstar' , 0),
    ('endstar' , 0),
    ('endgrade' , duanwei[22]),
    ('gamename' , '王者荣耀'),
    ('runeslevel' , 80),
    ('servername' , '默认服'),
    ('timestamp' , int(time.time()*1000))
]


parameters2 = [
    ['areaname' , '安卓-微信'],
    ['begingrade' , duanwei[0]],
    ['beginstar' , 0],
    ['endstar' , 0],
    ['endgrade' , duanwei[22]],
    ['gamename' , '王者荣耀'],
    ['runeslevel' , 80],
    ['servername' , '默认服'],
    ['timestamp' , int(time.time()*1000)]
]



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

headers = {'User-Agent':user_agent}
response={'data':1}


for i in range(len(duanwei)-1):
    parameters2[1][1] = duanwei[i]
    parameters2[4][1] = duanwei[i+1]


    search_data = urllib.parse.urlencode([tuple(x) for x in parameters2])
    request = urllib.request.Request(url,headers=headers,data=search_data.encode('utf-8'))
    with urllib.request.urlopen(request) as f:
        #print(eval(f.read().decode('utf-8')))
        #print(type)
        map = eval(f.read().decode('utf-8'))
        print('%s->%s:%s元' %(map['data']['begingrade'],map['data']['endgrade'],map['data']['price']))



