
from simulators.ds import run_ds_simulator
import threading
import time
from locks.print_lock import print_lock


def ds_callback(motion_detected, code):
    with print_lock:
        if motion_detected:
           t = time.localtime()
           print("="*20)
           print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
           print(f"Code: {code}")
           print(f"Motion detected\n")


def run_ds(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            ds_thread = threading.Thread(target = run_ds_simulator, args=(2, ds_callback, stop_event, code))
            ds_thread.start()
            threads.append(ds_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            ds_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, ds_callback, stop_event, code))
            ds_thread.start()
            threads.append(ds_thread)
            print(code + " loop started")
