
import threading
import time
from locks.print_lock import print_lock
from actuators.rgb import run
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
import json
from datetime import datetime, timedelta


rgb_batch = []
publish_data_counter = 0
publish_data_limit = 5
color = ''
is_on = False
def publisher_task(event, rgb_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with print_lock:
            local_batch = rgb_batch.copy()
            publish_data_counter = 0
            rgb_batch.clear()
        publish.multiple(local_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} rgb values')
        event.clear()


def rgb_callback(settings, publish_event):
    global color
    global is_on
    global publish_data_counter, publish_data_limit


    if result:
        result = False
    else:
        result = True
    current_datetime = datetime.now()

    adjusted_datetime = current_datetime - timedelta(hours=1)

    formatted_time = adjusted_datetime.isoformat()
    payload = {
        'measurement': 'Light',
        'simulated': settings['simulated'],
        'runs_on': settings['runs_on'],
        'name': settings['name'],
        'value': result,
        '_time': formatted_time
    }
    with print_lock:
        rgb_batch.append(('rgb', json.dumps(payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, rgb_batch,))
publisher_thread.daemon = True
publisher_thread.start()

def run_rgb(settings, threads, stop_event, code):
        if settings['simulated']:
            dl_thread = threading.Thread(target = rgb_callback, args=( settings, publish_event))
            dl_thread.start()
            threads.append(dl_thread)
        else:
            pin =settings['pin']
            dms_thread = threading.Thread(target=run, args=(pin,rgb_callback, stop_event, settings, publish_event))
            dms_thread.start()
            threads.append(dms_thread)
