import random
from datetime import datetime
from time import sleep
from elasticsearch import Elasticsearch

es = Elasticsearch(['elastic'])


while True:
    for i in xrange(random.randrange(1, 20)):
        es.index(index='metric', doc_type='metric', body={
            'metric_name': 'pizza',
            'timestamp': datetime.now(),
            })
    sleep(1)


