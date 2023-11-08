
import threading
import time
from locks.print_lock import print_lock2

result = True
def dl_callback(code):
    global result
    with print_lock2:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        if result:
            result = False
            print("Light is on\n")
        else:
            result = True
            print("Light is off\n")


def run_dl(settings, threads, stop_event, code):
        if settings['simulated']:
            dl_thread = threading.Thread(target = dl_callback, args=(code,))
            dl_thread.start()
            threads.append(dl_thread)
        else:
            from sensors.dht import run_dms_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            dms_thread = threading.Thread(target=run_dms_loop, args=(dht, 5, dms_callback, stop_event, code))
            dms_thread.start()
            threads.append(dms_thread)
            print(code + " loop started")
