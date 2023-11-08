
import threading
import time
from locks.print_lock import print_lock
from simulators.dms import run_dms_simulator


def dms_callback( result, code):
    with print_lock:

        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"User entered: " + str(result))


def run_dms(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            dms_thread = threading.Thread(target = run_dms_simulator, args=(5, dms_callback, stop_event, code))
            dms_thread.start()
            threads.append(dms_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.dht import run_dms_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            dms_thread = threading.Thread(target=run_dms_loop, args=(dht, 5, dms_callback, stop_event, code))
            dms_thread.start()
            threads.append(dms_thread)
            print(code + " loop started")
