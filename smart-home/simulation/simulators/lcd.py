import time
import random


def generate_value():
    while True:
        state_changed = random.randint(-5, 5)
        text_length = random.randint(5, 15)
        lcd_text = ''.join(
            (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()') for _ in
             range(text_length)))
        yield lcd_text
        if state_changed < 0:
            continue
        yield lcd_text


def run_lcd_simulator(delay, callback, stop_event, settings, publish_event):
    for generated_text in generate_value():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(generated_text, settings, publish_event)
        if stop_event.is_set():
            break