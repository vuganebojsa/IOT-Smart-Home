try:
    import RPi.GPIO as GPIO
except:
    pass
import time
from locks.print_lock import print_lock

def pressed_button(channel,callback, settings, publish_event):
    callback(True, settings, publish_event)

def press_button(pin, callback, stop_event, settings, publish_event):

    PORT_BUTTON = int(pin)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(PORT_BUTTON, GPIO.RISING, callback=lambda channel: pressed_button(channel, callback, settings, publish_event))
    input("Press any key to exit...")