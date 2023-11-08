
import threading
import time
from locks.print_lock import print_lock2


def db_callback(code):

    t = time.localtime()
    with print_lock2:
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print("Buzzzing\n")


def run_db(settings, threads, stop_event, code):
        if settings['simulated']:

            db_thread = threading.Thread(target=db_callback, args=(code,))
            db_thread.start()
            threads.append(db_thread)
        else:
            from sensors.dht import run_dms_loop, DHT
            print("Starting " + code + " loop")
            dht = DHT(settings['pin'])
            dms_thread = threading.Thread(target=run_dms_loop, args=(dht, 5, dms_callback, stop_event, code))
            dms_thread.start()
            threads.append(dms_thread)
            print(code + " loop started")
