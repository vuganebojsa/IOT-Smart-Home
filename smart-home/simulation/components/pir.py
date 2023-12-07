
from simulators.pir import run_pir_simulator
import threading
import time
from locks.print_lock import print_lock
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
import json
dht_batch = []
publish_data_counter = 0
publish_data_limit = 5


def publisher_task(event, pir_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with print_lock:
            local_pir_batch = pir_batch.copy()
            publish_data_counter = 0
            pir_batch.clear()
        publish.multiple(local_pir_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} pir values')
        event.clear()

def pir_callback(motion_detected, settings, publish_event):
    global publish_data_counter, publish_data_limit
    if motion_detected:
        payload = {
            'measurement': 'Motion',
            'simulated': settings['simulated'],
            'runs_on': settings['runs_on'],
            'name': settings['name'],
            'value': 1,
        }
        with print_lock:
            dht_batch.append(('pir', json.dumps(payload), 0, True))
            publish_data_counter += 1
        if publish_data_counter >= publish_data_limit:
            publish_event.set()

publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dht_batch,))
publisher_thread.daemon = True
publisher_thread.start()

def run_pir(settings, threads, stop_event):
        if settings['simulated']:
            pir_thread = threading.Thread(target = run_pir_simulator, args=(5, pir_callback, stop_event, settings, publish_event))
            pir_thread.start()
            threads.append(pir_thread)

        else:
            from sensors.pir import detect_motion
            pin = settings['pin']
            pir_thread = threading.Thread(target=detect_motion, args=(pin, pir_callback,stop_event, settings, publish_event))
            pir_thread.start()
            threads.append(pir_thread)

