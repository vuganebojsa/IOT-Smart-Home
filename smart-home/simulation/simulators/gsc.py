import time
import random


def generate_value():
    while True:
        angular_velocity = random.uniform(-180, 180)
        yield angular_velocity


def run_gsc_simulator(delay, callback, stop_event, settings, publish_event):
    for angular_velocity in generate_value():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(angular_velocity, settings, publish_event)
        if stop_event.is_set():
            break
