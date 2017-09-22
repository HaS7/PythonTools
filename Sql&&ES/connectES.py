__author__ = 'York'


from elasticsearch import Elasticsearch


class myEs():
    def __init__(self):
        self.es = Elasticsearch([{'host':'127.0.0.1','port':12118}])

    def getEs(self):
        return self.es




