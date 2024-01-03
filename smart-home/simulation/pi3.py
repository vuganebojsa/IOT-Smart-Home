
import threading
from settings import load_settings
from components.dht import run_dht
from components.pir import run_pir
from components.bir import run_bir
import time
from components.db import run_db
from locks.print_lock import print_lock
from components.b4sd import run_b4sd

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


def run_dht_threads(settings, threads, stop_event):
    rdht4_settings = settings['RDHT4']
    run_dht(rdht4_settings, threads, stop_event, 'RDHT4')

def run_pir_threads(settings, threads, stop_event):
    rpir4_settings = settings['RPIR4']
    run_pir(rpir4_settings, threads, stop_event)

def run_bir_threads(settings, threads, stop_event):
    bir_settings = settings['BIR']

    run_bir(bir_settings, threads, stop_event)

def run_bb_threads(settings, threads, stop_event):
    db_settings = settings["BB"]
    run_db(db_settings, threads, stop_event, "BB")


def run_b4sd_threads(settings, threads, stop_event):
    bir_settings = settings['B4SD']

    run_b4sd(bir_settings, threads, stop_event)

if __name__ == "__main__":
    print('Starting app')
    settings = load_settings('settingspi3.json')
    threads = []
    stop_event = threading.Event()
    pause_event = threading.Event()
    try:
        run_dht_threads(settings, threads, stop_event)
        run_pir_threads(settings, threads, stop_event)
        run_bir_threads(settings, threads, stop_event)
        run_b4sd_threads(settings, threads, stop_event)
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
