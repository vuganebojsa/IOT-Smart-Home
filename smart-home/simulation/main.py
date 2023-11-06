
import threading
from settings import load_settings
from components.dht import run_dht
from components.pir import run_pir
from components.dus import run_dus
import time
from components.dpir import run_dpir

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

def run_dpir_threads(settings, threads, stop_event):
    rpir1_settings = settings['DPIR1']

    run_dpir(rpir1_settings, threads, stop_event, 'DPIR1')

def run_dus_threads(settings, threads, stop_envet):
    dus1_settings = settings['DUS1']
    run_dus(dus1_settings, threads, stop_envet, 'DUS1')



if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        run_dht_threads(settings, threads, stop_event)
        run_pir_threads(settings, threads, stop_event)
        run_dpir_threads(settings, threads, stop_event)
        run_dus_threads(settings, threads, stop_event)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
