try:
    import RPi.GPIO as GPIO
except:
    pass
import time
from locks.print_lock import print_lock

def detect_motion(code, r1, r2, r3, r4, c1, c2, c3, c4):
    R1 = int(r1)
    R2 = int(r2)
    R3 = int(r3)
    R4 = int(r4)

    C1 = int(c1)
    C2 = int(c2)
    C3 = int(c3)
    C4 = int(c4)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    GPIO.setup(R3, GPIO.OUT)
    GPIO.setup(R4, GPIO.OUT)

    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def readLine(line, characters):
        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            with print_lock:
                print(characters[0])
        if(GPIO.input(C2) == 1):
            with print_lock:
                print(characters[1])
        if(GPIO.input(C3) == 1):
            with print_lock:
                print(characters[2])
        if(GPIO.input(C4) == 1):
            with print_lock:
                print(characters[3])
        GPIO.output(line, GPIO.LOW)

    while True:
        # call the readLine function for each row of the keypad
        readLine(R1, ["1","2","3","A"])
        readLine(R2, ["4","5","6","B"])
        readLine(R3, ["7","8","9","C"])
        readLine(R4, ["*","0","#","D"])
        time.sleep(0.2)

