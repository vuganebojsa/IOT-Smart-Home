from influxdb_client import Point


bucket_influx = "iot_smart_home"
org_influx = "FTN"


def write_dht(write_api, data):
    point = (
        Point(data["measurement_temperature"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value_temperature"])
        .time(data['_time'])

    )

    write_api.write(bucket=bucket_influx, org=org_influx, record=point)
    point = (
        Point(data["measurement_humidity"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value_humidity"])        
        .time(data['_time'])

    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dms(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(data['_time'])

    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_ds(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(data['_time'])

    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dus(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(data['_time'])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_pir(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(data['_time'])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_db(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
        .time(data['_time'])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dl(write_api, data):
    if data['value'] == True:
        data['value'] = 1
    elif data['value'] == False:
        data['value'] = 0
    if '_time' in data:
        point = (
            Point(data["measurement"])
            .tag("simulated", data["simulated"])
            .tag("runs_on", data["runs_on"])
            .tag("name", data["name"])
            .tag('_time', data['_time'])
            .field("measurement", data["value"])
            .time(data['_time'])
        )
        write_api.write(bucket=bucket_influx, org=org_influx, record=point)
