
import threading
from settings import load_settings
from components.dht import run_dht
from components.pir import run_pir
import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


def run_dht_threads(settings, threads, stop_event):
    rdht1_settings = settings['RDHT1']
    rdht2_settings = settings['RDHT2']
    run_dht(rdht1_settings, threads, stop_event, 'RDHT1')
    run_dht(rdht2_settings, threads, stop_event, 'RDHT2')

def run_pir_threads(settings, threads, stop_event):
    rpir1_settings = settings['RPIR1']
    rpir2_settings = settings['RPIR2']
    run_pir(rpir1_settings, threads, stop_event, 'RPIR1')
    run_pir(rpir2_settings, threads, stop_event, 'RPIR2')

if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        run_dht_threads(settings, threads, stop_event)
        run_pir_threads(settings, threads, stop_event)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
