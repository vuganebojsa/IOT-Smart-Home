try:
    import RPi.GPIO as GPIO
except:
    print('Cant load')
import time
from locks.print_lock import print_lock2
        
def run_light(pin, code):
    with print_lock2:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
    pin = int(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    print("Led On")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    print("Led Of")
    GPIO.output(pin, GPIO.LOW)
