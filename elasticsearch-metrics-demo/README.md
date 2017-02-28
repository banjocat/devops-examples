# Purpose
Just a quick demo of one way to use elasticsearch as a timeseries database

## Why use elasticsearch as a timeseries database?
* To simplify your stack.
* Elasticsearch is a swiss army knife
* Better horizontal scaling compared to graphite

## Conclusion
My two favorite database tools are postgres and elasticsearch.
They compliment each other very well. For very high elasticsearch writes
I would add logstash and filebeat. For even more througput I would add kafka.

