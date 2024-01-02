import threading
import time
from locks.print_lock import print_lock
from datetime import datetime, timedelta

from simulators.gsc import run_gsc_simulator
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
import json
dht_batch = []
publish_data_counter = 0
publish_data_limit = 5


def publisher_task(event, gsc_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with print_lock:
            local_gsc_batch = gsc_batch.copy()
            publish_data_counter = 0
            gsc_batch.clear()
        publish.multiple(local_gsc_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} gsc values')
        event.clear()

def gsc_callback(motion_detected, settings, publish_event):
    global publish_data_counter, publish_data_limit
    if motion_detected:
        current_datetime = datetime.now()

        adjusted_datetime = current_datetime - timedelta(hours=1)

        formatted_time = adjusted_datetime.isoformat()
        payload = {
            'measurement': 'Rotation',
            'simulated': settings['simulated'],
            'runs_on': settings['runs_on'],
            'name': settings['name'],
            'value': 1,
            '_time': formatted_time
        }
        with print_lock:
            dht_batch.append(('gsc', json.dumps(payload), 0, True))
            publish_data_counter += 1
        if publish_data_counter >= publish_data_limit:
            publish_event.set()

publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dht_batch,))
publisher_thread.daemon = True
publisher_thread.start()

def run_gsc(settings, threads, stop_event):
        if settings['simulated']:
            gsc_thread = threading.Thread(target=run_gsc_simulator,
                                          args=(5, gsc_callback, stop_event, settings, publish_event))
            gsc_thread.start()
            threads.append(gsc_thread)
        else:
            from sensors.gsc import detect_motion
            sda = settings['SDA']
            scl = settings['SCL']
            dpir_thread = threading.Thread(target=detect_motion,
                                          args=(sda, scl, gsc_callback, stop_event, settings, publish_event))
            dpir_thread.start()
            threads.append(dpir_thread)
