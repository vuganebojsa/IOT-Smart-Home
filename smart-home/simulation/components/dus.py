
import threading
import time
from locks.print_lock import print_lock
from simulators.dus import run_dus_simulator


def dus_callback(distance, code):
    with print_lock:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"Distance: " + str(distance) + " cm")


def run_dus(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            dus_thread = threading.Thread(target = run_dus_simulator, args=(5, dus_callback, stop_event, code))
            dus_thread.start()
            threads.append(dus_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            pir_thread = threading.Thread(target=run_dht_loop, args=(dht, 5, dus_callback, stop_event, code))
            pir_thread.start()
            threads.append(pir_thread)
            print(code + " loop started")
