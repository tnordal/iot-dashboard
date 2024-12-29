import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import dotenv
import os

dotenv.load_dotenv()

# InfluxDB connection details
bucket = os.getenv("influxdb_bucket")  
org = os.getenv("influxdb_org")
token = os.getenv("influxdb_token")
url = os.getenv("influxdb_url")

# Debug prints to verify environment variables
print(f"Bucket: {bucket}")
print(f"Org: {org}")
print(f"Token: {token}")
print(f"URL: {url}")

# Create a client
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org, debug=True)
query_api = client.query_api()

# Verify client initialization
print(f"Client: {client}")

def get_topics():
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -1h, stop: now())
      |> keep(columns: ["topic"])
      |> group()
      |> distinct(column: "topic")
    '''
    print(f"Query: {query}")
    
    result = query_api.query(org=org, query=query)
    topics = [record.get_value() for table in result for record in table.records]
    return topics

def get_fields_for_topic(topic):
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -24h, stop: now())
      |> filter(fn: (r) => r["_measurement"] == "{topic}")
      |> keep(columns: ["_field"])
      |> distinct()
    '''
    print(f"Query: {query}")
    
    result = query_api.query(org=org, query=query)
    print(f"Raw Result: {result}")
    
    fields = [record.get_value() for table in result for record in table.records]
    print(f"Fields: {fields}")
    
    return fields

def get_data_for_topic_and_field(topic, field):
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -1h, stop: now())
      |> filter(fn: (r) => r["_field"] == "{field}")
      |> filter(fn: (r) => r["_measurement"] == "{topic}")
      |> aggregateWindow(every: 2m, fn: mean, createEmpty: false)
      |> yield(name: "mean")
    '''
    print(f"Query: {query}")
    
    result = query_api.query(org=org, query=query)
    data = [(record.get_time(), record.get_value()) for table in result for record in table.records]
    return data

# Close the client
client.close()