import time
import random
current_state = False
button_pressed_time = None
def generate_value():

    while True:
        state_changed = random.randint(-5, 5)
        if state_changed < 3:
            current_state = True
        else:
            current_state = False

        yield current_state


def run_ds_simulator(delay, callback, stop_event, settings, publish_event):
    global button_pressed_time
    past_value = False

    for motion in generate_value():
        if motion :
            if past_value == False:
                button_pressed_time = time.time()
                past_value = True
        else:
            if past_value == True:

                if button_pressed_time is not None and (time.time() - button_pressed_time) > 5:
                    print("ALARM: Dugme pritisnuto duže od 5 sekundi")
                button_pressed_time = None
                past_value = False
        time.sleep(delay)
        print(motion)
        callback(motion, settings, publish_event)

        if stop_event.is_set():
            break
