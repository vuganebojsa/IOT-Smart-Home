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
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)
    point = (
        Point(data["measurement_humidity"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value_humidity"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dms(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_ds(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dus(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_pir(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_db(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)

def write_dl(write_api, data):
    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket_influx, org=org_influx, record=point)
