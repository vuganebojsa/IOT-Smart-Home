
import threading
import time
from locks.print_lock import print_lock2
from actuators.dl import run_dl
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
            pin =settings['pin']
            dms_thread = threading.Thread(target=run_dl, args=(pin, code))
            dms_thread.start()
            threads.append(dms_thread)
            print(code + " loop started")
