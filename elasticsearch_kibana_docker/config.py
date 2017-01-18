mapping = """curl -XPUT "http://localhost:9200/airports" -d'
{
  "mappings": {
    "airport": {
      "properties" : {
          "lat_lon" : {"type" : "geo_point"},
          "elevation_ft" : {"type" : "integer"},
          "airport_type" : {"type": "string", "index" : "not_analyzed"},
          "wikipedia_link" : {"type": "string", "index" : "not_analyzed"}
      }
    }
  }
}'"""

bulk_index = 'curl -s -XPOST localhost:9200/airports/airport/_bulk --data-binary @data_preprocessing/data.json;'

docker_run = 'docker run -p 9200:9200 -p 9300:9300 -p 5601:5601 -t -i -d'

cluster_health = "curl -XGET 'http://localhost:9200/_cluster/health'"

image  = 'alcedok/elastic_kibana_docker:v1'