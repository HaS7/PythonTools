#coding=utf-8
__author__ = 'York'



import os
import re

#              <type name="goods_type_type" class="int" code="10010"/>
#            <field name="sess_b_uid" type="sess_b_uid_type" />

#'C:/Users/Administrator/Desktop/脚本文件库/new 1.txt'
def change(path,code=1):
    pattern = re.compile('.*?name="(.*?)"')
    arr = []
    with open(path,'r') as f_r:
        flag = False
        for line in f_r.readlines():
            if(line.strip().startswith('<responseParameter>')):
                flag=True
            if(line.strip().startswith('<field') and flag):
                target = re.findall(pattern,line.strip())[0]
                #print('<type name="%s"  class="%s" code="%d"/>'% (target,'string',code))
                arr.append(target)

                code+=1
    #print(arr)
    return arr


#print(change())

#print(change())


def compareArr(arr1,arr2):
    same = []
    differ = []
    for x in arr1:
        if x in arr2:
            same.append(x)
        else:
            differ.append(x)
    for x in arr2:
        if x not in arr1:
            differ.append(x)
    same.extend(differ)
    return same


path1 = 'C:/Users/Administrator/Desktop/脚本文件库/new 1.txt'
path2 = 'C:/Users/Administrator/Desktop/脚本文件库/2.txt'
arr = compareArr(change(path1), change(path2))
#<field name="sess_b_uid" type="sess_b_uid_type" />
def printField(arr,path):
    with open(path,'w') as f:
        for target in arr:
            f.write('<field name="%s" type="%s" />%s'% (target,target+"_type",'\n'))
path = 'C:/Users/Administrator/Desktop/脚本文件库/ret.txt'

printField(compareArr(change(path1), change(path2)),path)

#print(change(path1))

#f = open('C:/Users/Administrator/Desktop/脚本文件库/2.txt','r')
#print(f.read())

# with open('/path/to/file', 'r') as f:
#     print(f.read())
#f.write('Hello, world!')


#f.close()
