
from simulators.pir import run_pir_simulator
import threading
import time
from locks.print_lock import print_lock


def pir_callback(motion_detected, code):
    with print_lock:
        if motion_detected:
           t = time.localtime()
           print("="*20)
           print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
           print(f"Code: {code}")
           print(f"Motion detected\n")


def run_pir(settings, threads, stop_event, code):
        if settings['simulated']:
            print("Starting " + code + " sumilator")
            pir_thread = threading.Thread(target = run_pir_simulator, args=(5, pir_callback, stop_event, code))
            pir_thread.start()
            threads.append(pir_thread)
            print(code + " sumilator started\n")
        else:
            from sensors.pir import detect_motion
            print("Starting " + code + " loop")
            pin = settings['pin']
            pir_thread = threading.Thread(target=detect_motion, args=(pin, code))
            pir_thread.start()
            threads.append(pir_thread)
            print(code + " loop started")
