import time
import datetime




def countdown(s, pen,game):
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    curr_time =time.time()
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
    pen.clear()    
    if game.player1Points > game.player2Points:
       pen.write("Player 1 WINS", align="center", font=("Courier", 24, "normal"))
    elif game.player1Points < game.player2Points:
        pen.write("Player 2 WINS", align="center", font=("Courier", 24, "normal")) 
    else:
        pen.write("DRAW", align="center", font=("Courier", 24, "normal"))