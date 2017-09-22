__author__ = 'Administrator'

# 10.240.17.237/10.240.17.238 两台虚拟机的 用户名/密码 ：  root/WD#sd7258  ,ssh 端口：58422
#
# 服务端口：12439
# host = kw.get('host', 'localhost'),
# port = kw.get('port', 3306),
# user = kw['user'],
# password = kw['password'],
# db = kw['db'],
# charset = kw.get('charset', 'utf8'),
# autocommit = kw.get('autocommit', True),
# maxsize = kw.get('maxsize', 10),
# minsize = kw.get('minsize', 1),
# loop = loop

configs = {
    'db':{
        'host':'10.240.17.237',
        'port':3306,
        'user':'root',
        'password':'WD#sd7258',
        'db':'test',
    }


}
