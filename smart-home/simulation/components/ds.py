
from simulators.ds import run_ds_simulator
import threading
import time
from locks.print_lock import print_lock


current_value = True
def ds_callback(state_changed, code):
    global current_value
    with print_lock:
        if state_changed:
            if current_value == True:
                current_value = False
                t = time.localtime()
                print("=" * 20)
                print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
                print(f"Code: {code}")
                print(f"Door opened\n")
            else:
                current_value = True
                t = time.localtime()
                print("=" * 20)
                print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
                print(f"Code: {code}")
                print(f"Door closed\n")




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
