import RPi.GPIO as GPIO
from locks.print_lock import print_lock
import time

def motion_detected(channel):
    print("You moved")
def no_motion(channel):
    print("You stopped moving")


def detect_motion(pin, code):
    with print_lock:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
    PIR_PIN = int(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion_detected)
    GPIO.add_event_detect(PIR_PIN, GPIO.FALLING, callback=no_motion)
    input("Press any key to exit...")

