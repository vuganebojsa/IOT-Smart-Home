
import threading
from settings import load_settings
from components.dht import run_dht
from components.pir import run_pir
import time
from components.db import run_db
from locks.print_lock import print_lock

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

    #run_dpir(bir_settings, threads, stop_event)

def run_bb_threads(settings, threads, stop_event):
    db_settings = settings["BB"]
    run_db(db_settings, threads, stop_event, "BB")



def menu(stop_event):
    while not stop_event.is_set():
        user_input = input("Press 'm' to open the menu: ")
        print("user input: ", user_input)
        if user_input == "m":
            while True:
                with print_lock:
                    print("Menu Options:")
                    print("Press l to control Door Light")
                    print("Press b to control Bedroom Buzzer")
                    print("Press 'e' to exit the menu")
                    user_input = input("Enter your choice: ")
                    if user_input == "l":
                        #run_dl_threads(settings, threads, stop_event)
                        time.sleep(1)
                    elif user_input == "b":
                        run_bb_threads(settings, threads, stop_event)
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
    settings = load_settings('settingspi3.json')
    threads = []
    stop_event = threading.Event()
    pause_event = threading.Event()
    try:
        run_dht_threads(settings, threads, stop_event)
        run_pir_threads(settings, threads, stop_event)
        run_bir_threads(settings, threads, stop_event)
        run_menu_thread(threads, stop_event)
        while True:
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
