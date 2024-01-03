
from simulators.ds import run_ds_simulator
import threading
import time
from locks.print_lock import print_lock
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
import json
from datetime import datetime, timedelta

dht_batch = []
publish_data_counter = 0
publish_data_limit = 5

def publisher_task(event, dht_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with print_lock:
            local_dht_batch = dht_batch.copy()
            publish_data_counter = 0
            dht_batch.clear()
        publish.multiple(local_dht_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} ds values')
        event.clear()

def ds_callback(current_value, settings,publish_event):
    global publish_data_counter, publish_data_limit
    value = 0
    if current_value is True:
        value = 1
    current_datetime = datetime.now()

    adjusted_datetime = current_datetime - timedelta(hours=1)

    formatted_time = adjusted_datetime.isoformat()
    payload = {
        'measurement': 'Pressed',
        'simulated': settings['simulated'],
        'runs_on': settings['runs_on'],
        'name': settings['name'],
        'value': value,
        '_time': formatted_time
    }
    with print_lock:
        dht_batch.append(('ds', json.dumps(payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dht_batch,))
publisher_thread.daemon = True
publisher_thread.start()

def run_ds(settings, threads, stop_event, code):
        if settings['simulated']:
            ds_thread = threading.Thread(target = run_ds_simulator, args=(1, ds_callback, stop_event, settings, publish_event))
            ds_thread.start()
            threads.append(ds_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.ds import press_button
            pin = settings['pin']
            ds_thread = threading.Thread(target=press_button,
                                          args=(pin, ds_callback, stop_event, settings, publish_event))
            ds_thread.start()
            threads.append(ds_thread)
