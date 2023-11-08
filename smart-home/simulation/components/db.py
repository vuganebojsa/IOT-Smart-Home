
import threading
import time
from locks.print_lock import print_lock2
from actuators.db import buzz

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
            pin =settings['pin']
            db_thread = threading.Thread(target=buzz, args=(pin, code))
            db_thread.start()
            threads.append(db_thread)
            print(code + " loop started")
