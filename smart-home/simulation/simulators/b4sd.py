import time
import random

def generate_value():
      while True:
        current_time = time.strftime("%H %M")
        yield current_time

              
def run_b4sd_simulator(delay, callback, stop_event, settings, publish_event):
    for value in generate_value():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(value, settings, publish_event)
        if stop_event.is_set():
            break
            