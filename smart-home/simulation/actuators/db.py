try:
    import RPi.GPIO as GPIO
except:
    print('Cant laod')
import time
from locks.print_lock import print_lock2

def buzz(pin, code):
    with print_lock2:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
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
    time.sleep(1)
