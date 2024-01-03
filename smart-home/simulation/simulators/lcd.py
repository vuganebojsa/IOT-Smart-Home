import time
import random


def generate_value(msg):
    while True:
        lcd_text = msg
        yield lcd_text


def run_lcd_simulator(delay, callback, stop_event, settings, publish_event, msg):
    for generated_text in generate_value(msg):
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(generated_text, settings, publish_event)
        if stop_event.is_set():
            break