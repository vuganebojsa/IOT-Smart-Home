import time
import random


def generate_value():
    current_state = True
    while True:
        state_changed = random.randint(-5, 5)
        if state_changed < -3:
            if current_state:
                current_state = False
            else:
                current_state = True
            yield current_state


def run_ds_simulator(delay, callback, stop_event, code):
    for motion in generate_value():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(motion, code)
        if stop_event.is_set():
            break
