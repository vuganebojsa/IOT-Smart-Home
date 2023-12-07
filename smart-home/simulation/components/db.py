
import threading
import time
from locks.print_lock import print_lock
from actuators.db import buzz

import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
import json

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
        print(f'published {publish_data_limit} db values')
        event.clear()


def db_callback(settings, publish_event):
    global result
    global publish_data_counter, publish_data_limit

    payload = {
        'measurement': 'Buzz',
        'simulated': settings['simulated'],
        'runs_on': settings['runs_on'],
        'name': settings['name'],
        'value': "Buzzing"
    }
    with print_lock:
        dht_batch.append(('db', json.dumps(payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dht_batch,))
publisher_thread.daemon = True
publisher_thread.start()

def run_db(settings, threads, stop_event, code):
        if settings['simulated']:

            db_thread = threading.Thread(target=db_callback, args=(settings, publish_event))
            db_thread.start()
            threads.append(db_thread)
        else:
            pin =settings['pin']
            db_thread = threading.Thread(target=buzz, args=(pin,db_callback, stop_event, settings, publish_event))
            db_thread.start()
            threads.append(db_thread)
            print(code + " loop started")
