import threading
import time
from locks.print_lock import print_lock

from simulators.dpir import run_dus_simulator


def dpir_callback(motion_detected, code):
    with print_lock:
        if motion_detected:
           t = time.localtime()
           print("="*20)
           print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
           print(f"Code: {code}")
           print(f"Motion detected\n")


def run_dpir(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            dpir_thread = threading.Thread(target = run_dus_simulator, args=(5, dpir_callback, stop_event, code))
            dpir_thread.start()
            threads.append(dpir_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            pir_thread = threading.Thread(target=run_dht_loop, args=(dht, 5, dpir_callback, stop_event, code))
            pir_thread.start()
            threads.append(pir_thread)
            print(code + " loop started")
