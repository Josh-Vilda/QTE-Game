import time
import datetime
import turtle




def countdown(s, pen):
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while s >= 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = s)
       
        # Prints the time left on the timer
        pen.clear()
        pen.write("Time: {}".format(timer), align="center", font=("Courier", 24, "normal"))
        # Delays the program one second
        time.sleep(1)
        # Reduces total time by one second
        s -= 1
    print("Bzzzt! The countdown is at zero seconds!")