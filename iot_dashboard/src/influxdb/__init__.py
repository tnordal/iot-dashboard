# This file is intentionally left blank.
from influxdb_client import InfluxDBClient

influxdb_client = InfluxDBClient(url="http://localhost:8086", token="your-token", org="your-org")  # Change to your InfluxDB configuration

def get_data(room):
    query = f'from(bucket: "iot_data") |> range(start: -1h) |> filter(fn: (r) => r["_measurement"] == "{room}")'
    result = influxdb_client.query_api().query(query)
    return result

def write_command(command):
    write_api = influxdb_client.write_api()
    point = {
        "measurement": "iot_commands",
        "fields": {
            "command": command
        }
    }
    write_api.write(bucket="iot_commands", record=point)