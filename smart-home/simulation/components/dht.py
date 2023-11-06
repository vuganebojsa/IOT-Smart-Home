
from simulators.dht import run_dht_simulator
import threading
import time
from locks.print_lock import print_lock


def dht_callback(humidity, temperature, code):
    with print_lock:
        print(code + ' readings')
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"Humidity: {humidity}%")
        print(f"Temperature: {temperature}°C\n")


def run_dht(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            dht_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event, code))
            dht_thread.start()
            threads.append(dht_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.dht import run_dht_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            dht_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event, code))
            dht_thread.start()
            threads.append(dht_thread)
            print(code + " loop started")
