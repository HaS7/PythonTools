__author__ = 'York'


from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'127.0.0.1','port':12118}])

#create index
#es.indices.create()

mapping = {
  "logs": {
    "_all": {
      "analyzer": "ik"
    },
    "properties": {
      "path": {
        "type": "string"
      },
      "@timestamp": {
        "format": "strict_date_optional_time||epoch_millis",
        "type": "date"
      },
      "@version": {
        "type": "string"
      },
      "host": {
        "type": "string"
      },
      "message": {
        "include_in_all": True,
        "analyzer": "ik",
        "term_vector": "with_positions_offsets",
        "boost": 8,
        "type": "string",
        "fielddata" : { "format" : "true" }
      },
      "tags": {
        "type": "string"
      }
    }
  }
}
#es.indices.put_mapping('logs',mapping1,index='york-index',update_all_types=True)


query_body = {
    "size": 0,
    "aggs": {
        "message": {
            "terms": {
                "size": 100,
                "field": "p_values",
                "include" : "[\u4E00-\u9FA5]{2,}"
            }
        }
    }
}

ret = es.search(index='gmm_mixed_product_index_136_ik_v2',body=query_body)

print(ret)
# list1 = ret['aggregations']['messages']['buckets']
#
# for i in list1:
#     print(str(i)+'\n')
#
# from matplotlibTest import draw
#
# draw(list1[:10])



