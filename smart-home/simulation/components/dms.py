
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
            from sensors.dms import detect_motion
            print("Starting " + code + " loop")
            r1 = settings['R1']
            r2 = settings['R2']
            r3 = settings['R3']
            r4 = settings['R4']
            c1 = settings['C1']
            c2 = settings['C2']
            c3 = settings['C3']
            c4 = settings['C4']
            pir_thread = threading.Thread(target=detect_motion, args=(code, r1, r2, r3, r4, c1, c2, c3, c4))
            pir_thread.start()
            threads.append(pir_thread)
            print(code + " loop started")
