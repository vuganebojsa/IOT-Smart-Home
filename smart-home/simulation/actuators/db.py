try:
    import RPi.GPIO as GPIO
except:
    print('Cant load')
import time
from locks.print_lock import print_lock2

def buzz(pin, callback, stop_event, settings, publish_event):
    pin = int(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    pitch = 440
    duration = 0.1
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(pin, True)
        time.sleep(delay)
        GPIO.output(pin, False)
        time.sleep(delay)
    callback(settings, publish_event)
    time.sleep(1)
