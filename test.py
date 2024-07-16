from datahub.ingestion.graph.client import DatahubClientConfig, DataHubGraph
import sys

gms_endpoint = "http://localhost:8080"
graph = DataHubGraph(DatahubClientConfig(server=gms_endpoint))

API = sys.argv[1]
flag = sys.argv[2]
arguments = sys.argv[3:]
# Query multiple aspects from entity

query = 'mutation updateLineage {updateLineage(input: {edgesToAdd: ['
if flag =="up":
   for arg in arguments:
      query = query + '{downstreamUrn: "urn:li:dataset:(urn:li:dataPlatform:go-API,' + API + ',PROD)",' 
      query = query +   'upstreamUrn: "urn:li:dataset:(urn:li:dataPlatform:postgres,mydatabase.public.'+ arg +',PROD)"}'
   query = query + '], edgesToRemove: []})}'

elif flag =="down":
   for arg in arguments:
      query = query + '{downstreamUrn: "urn:li:dataset:(urn:li:dataPlatform:postgres,mydatabase.public.'+ arg +',PROD)",' 
      query = query +   'upstreamUrn: "urn:li:dataset:(urn:li:dataPlatform:go-API,' + API + ',PROD)"}'
   query = query + '], edgesToRemove: []})}'

result = graph.execute_graphql(query=query)

print(result)



