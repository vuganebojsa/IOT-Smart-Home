
import threading
from settings import load_settings
from components.dht import run_dht
from components.pir import run_pir
from components.dus import run_dus
import time
from components.dpir import run_dpir
from components.ds import run_ds
from components.dms import run_dms
from components.dl import run_dl
from components.db import run_db
from components.gsc import run_gsc

from locks.print_lock import print_lock

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


def run_dht_threads(settings, threads, stop_event):
    gdht1_settings = settings['GDHT']
    run_dht(gdht1_settings, threads, stop_event, 'GDHT')
    rdht3_settings = settings['RDHT3']
    run_dht(rdht3_settings, threads, stop_event, 'RDHT3')


def run_pir_threads(settings, threads, stop_event):
    rpir3_settings = settings['RPIR3']

    run_pir(rpir3_settings, threads, stop_event)

def run_dpir_threads(settings, threads, stop_event):
    dpir2_settings = settings['DPIR2']

    run_dpir(dpir2_settings, threads, stop_event)

def run_ds_threads(settings, threads, stop_event):
    ds2_settings = settings['DS2']
    run_ds(ds2_settings, threads, stop_event, 'DS2')

def run_dus_threads(settings, threads, stop_event):
    dus2_settings = settings['DUS2']
    run_dus(dus2_settings, threads, stop_event)

def run_gsc_threads(settings, threads, stop_event):
    db_settings = settings["GSC"]
    run_gsc(db_settings, threads, stop_event)

def run_lcd_threads(settings, threads, stop_event):
    db_settings = settings["GLCD"]
    run_lcd(db_settings, threads, stop_event)



def menu(stop_event):
    while not stop_event.is_set():
        user_input = input("Press 'm' to open the menu: ")
        print("user input: ", user_input)
        if user_input == "m":
            while True:
                with print_lock:
                    print("Menu Options:")
                    print("Press l to control Door Light")
                    print("Press b to control Door Buzzer")
                    print("Press 'e' to exit the menu")
                    user_input = input("Enter your choice: ")
                    if user_input == "l":
                        run_dl_threads(settings, threads, stop_event)
                        time.sleep(1)
                    elif user_input == "b":
                        run_db_threads(settings, threads, stop_event)
                        time.sleep(1)
                    elif user_input == "e":
                        print("Exiting the menu. Printing is resumed.")
                        break
        else:
            pass
def run_menu_thread(threads, stop_event):
    thread = threading.Thread(target = menu, args=(stop_event,))
    thread.start()
    threads.append(thread)

if __name__ == "__main__":
    print('Starting app')
    settings = load_settings('settingspi2.json')
    threads = []
    stop_event = threading.Event()
    pause_event = threading.Event()
    try:
        run_dht_threads(settings, threads, stop_event)
        run_pir_threads(settings, threads, stop_event)
        run_dpir_threads(settings, threads, stop_event)
        run_ds_threads(settings, threads, stop_event)
        run_dus_threads(settings, threads, stop_event)
        run_gsc_threads(settings, threads,  stop_event)
        run_lcd_threads(settings,threads,stop_event)
        run_menu_thread(threads, stop_event)

        while True:
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
