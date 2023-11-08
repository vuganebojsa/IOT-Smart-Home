try:
    import RPi.GPIO as GPIO
except:
    pass
import time
from locks.print_lock import print_lock

def pressed_button(channel):
    print("You pressed button")

def press_button(pin, code):
    with print_lock:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
    PORT_BUTTON = int(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(PORT_BUTTON, GPIO.RISING, callback =
    pressed_button, bouncetime = 100)
    input("Press any key to exit...")