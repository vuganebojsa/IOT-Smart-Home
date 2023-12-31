import time
import random

def generate_value():
      while True:
            motion_detected = random.randint(-5, 5)
            ret_motion = True
            if motion_detected < 2:
                 ret_motion = False
            yield ret_motion

              
def run_pir_simulator(delay, callback, stop_event, code):
    for motion in generate_value():
        time.sleep(delay)  # Delay between readings (adjust as needed)
        callback(motion, code)
        if stop_event.is_set():
            break
            