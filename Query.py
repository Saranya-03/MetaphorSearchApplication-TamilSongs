from elasticsearch import Elasticsearch

# Query used to search a property with a query value. It's a match query and return any word match in a whole phrase.
def search_with_field_any_match(query, field):
    q = {
        "query": {
            "match": {
                field: query
            }
        }
    }
    return q

# Query used in finding metaphors based on the selected fields. Since "உருவக அணி" வகை is a keyword type, we can use filter in bool search.
def bool_query(queryList):
    
    q ={
        "query": {
            "bool" : {
                "must" : [
                    {
                        "match" : { "இலக்கு" : {"query" : queryList["inputTarget"] }},
                        "match":{
                        "மூலப்பொருள்":{"query" :queryList["sourceDom"] }}
                }],
                "filter": {
                    "term" : { "உருவக அணி வகை": queryList["inputType"] }
                }
            }
        }
    }
    return q

# Generate query to search documents based on a set of properties, return documents in which anyone of them match with the query
def multi_match(query):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["உருவக அணி","உருவக அணி வகை","மூலப்பொருள்","இலக்கு","விளக்கம்"],
                "type": "best_fields"
            }
        }
    }
    return q

# Do interval search with max_gap =5 and order is not a matter.
def interval_query(query, field):
    q = {
        "query": {
            "intervals": {
                field: {
                    "match": {
                    "query": query,
                    "max_gaps": 5,
                    "ordered": False
                    }
                }
            }
        }
    }
    return q
    

def search_query(query):
    elasticSearch = Elasticsearch(HOST="http://localhost", PORT=9200)
    indexName = 'metaphors_db'
    print("Processing query...")
    if  (isinstance(query, str)) :
        createdQuery = interval_query(query,"உருவக அணி")
        resp = elasticSearch.search(index=indexName, body=createdQuery)
        if resp['hits']['total']['value']==0:
            createdQuery = search_with_field_any_match(query,"உருவக அணி")
            resp = elasticSearch.search(index=indexName, body=createdQuery)
            if resp['hits']['total']['value']==0:
                createdQuery = multi_match(query)
                resp = elasticSearch.search(index=indexName, body=createdQuery)
    else:
        createdQuery = bool_query(query)       
        resp = elasticSearch.search(index=indexName, body=createdQuery)    
    
    return resp