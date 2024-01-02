from flask import Flask, jsonify, request
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json
from influx_writes import *
import paho.mqtt.publish as publish
app = Flask(__name__)


# InfluxDB Configuration
users_inside = 0
alarm_active = False
system_active = False
token = "en1PQdEjc5Mqqct6lrc7lCO_7EDQc2auk6GMMKykVFMIPyD0gBPVE1UYj92RPW9h9mrKwzqR0QN6-iLttvJDGg=="
org = "FTN"
url = "http://localhost:8086"
bucket = "iot_smart_home"
influxdb_client = InfluxDBClient(url=url, token=token, org=org)
HOSTNAME = "localhost"
PORT = 1883

# MQTT Configuration

def on_connect(client, userdata, flags, rc):
    client.subscribe("dht")
    client.subscribe("dms")
    client.subscribe("ds")
    client.subscribe("dus")
    client.subscribe("pir")
    client.subscribe("db")
    client.subscribe("dl")


def save_to_db(topic, data):
    global users_inside
    global alarm_active
    write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    if topic == 'dht':

        if data['name'] == 'GDHT':
            dht_message = "humidity: " + str(data["value_humidity"]) + ", " + "temperature: " + str(data["value_temperature"])
            print(dht_message)
            publish.single('dht-lcd-display', json.dumps({'temperature':dht_message}), hostname=HOSTNAME, port=PORT)
        write_dht(write_api, data)
    elif topic == 'dms':
        write_dms(write_api, data)
    elif topic == 'ds':
        write_ds(write_api, data)
    elif topic == 'dus':
        write_dus(write_api, data)
    elif topic == 'pir':
        print(data['name'])
        print(users_inside)
        if 'RPIR' in data['name']:
            if users_inside == 0:
                alarm_active = True
                write_alarm_query(write_api, data['name'], data['_time'], alarm_active, data['name'] + ' detected movement.', data['simulated'])
            return
        query_data = []
        if data['name'] == 'DPIR1':
            query = f"""from(bucket: "{bucket}")
            |> range(start: -40s)
            |> filter(fn: (r) => r._measurement == "Distance")
            |> filter(fn: (r) => r["name"] == "DUS1")
            |> limit(n: 2)"""
            query_data = handle_influx_query(query)
            publish.single('dpir1-light-on', json.dumps({'light':'on'}), hostname=HOSTNAME, port=PORT)
        elif data['name'] == 'DPIR2':
            query = f"""from(bucket: "{bucket}")
            |> range(start: -40s)
            |> filter(fn: (r) => r._measurement == "Distance")
            |> filter(fn: (r) => r["name"] == "DUS2")
            |> limit(n: 2)"""
            query_data = handle_influx_query(query)
        is_entering = False
        if len(query_data['data']) > 1:
            if query_data['data'][0]['_value'] > query_data['data'][1]['_value']:
                is_entering = True
            if is_entering:
                users_inside += 1
            else:
                users_inside -= 1
        if users_inside < 0:
            users_inside = 0
        write_pir(write_api, data)
    elif topic == 'db':
        write_db(write_api, data)
    elif topic == 'dl':
        write_dl(write_api, data)

def handle_influx_query(query):
    try:
        query_api = influxdb_client.query_api()
        tables = query_api.query(query, org=org)

        container = []
        for table in tables:
            for record in table.records:
                container.append(record.values)

        return {"status": "success", "data": container}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.route('/simple_query', methods=['GET'])
def retrieve_simple_data():
    query = f"""from(bucket: "{bucket}")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "Light")"""
    return handle_influx_query(query)


if __name__ == '__main__':
    mqtt_client = mqtt.Client()
    mqtt_client.connect("localhost", 1883, 60)
    mqtt_client.loop_start()
    
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = lambda client, userdata, msg: save_to_db(msg.topic, json.loads(msg.payload.decode('utf-8')))

    app.run(debug=True)
