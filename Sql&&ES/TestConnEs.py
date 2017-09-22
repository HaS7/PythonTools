__author__ = 'Administrator'

from datetime import datetime

from elasticsearch import Elasticsearch



def queryES(index,body):

    es = Elasticsearch([{'host':'127.0.0.1','port':12118}])

    return es.search(index=index,body=body)



