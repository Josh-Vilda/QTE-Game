from arrows import ArrowsP1, ArrowsP2
import random
import keyboard
import time

class GameState:

    def __init__(self,pen) -> None:
        self.pen = pen # the pen we change the image of
        self.player1Points = 0
        self.player2Points = 0
        self.spamP1 =0
        self.spamP2 =0
        self.currentDirection = " "
        self.isClear = False
        
        
    def blank(self):
        self.isClear = True
        self.pen.shape("assets/clear.gif")    
        self.currentDirection =""
        print(">CLEAR")
        
    def up(self):
        self.pen.shape("assets/up.gif")
        self.currentDirection ="UP"
        print(">UP")
        
    def down(self):
        self.pen.shape("assets/down.gif")
        self.currentDirection ="DOWN"
        self.isClear = True
        print(">DOWN")


    def right(self):
        self.pen.shape("assets/right.gif")
        self.currentDirection ="RIGHT"
        self.isClear = True
        print(">RIGHT")


    def left(self):
        self.pen.shape("assets/left.gif")
        self.currentDirection ="LEFT"
        self.isClear = True
        print(">LEFT")


    def randomizer(self):
        print("> we random")    
        num = random.randint(0, 3)
        if num == 0:
            self.up()
        elif num == 1:
            self.down()
        elif num == 2:
            self.right()
        elif num == 3:
            self.left()
                   
                            
    def player1GotPoint(self,p1pm):
        print("Player 1 got point")
        self.player1Points += 1
        #writing the score 
        p1pm.ht()
        p1pm.goto(500,260)
        p1pm.clear()    
        p1pm.write("P1: {}".format(self.player1Points), align="center", font=("Courier", 24, "normal"))

    def player2GotPoint(self,p2pm):
        print("player 2 got point")
        self.player2Points += 1
        #writing the score 
        p2pm.ht()
        p2pm.goto(-500,260)
        p2pm.clear()
        p2pm.write("P2: {}".format(self.player2Points), align="center", font=("Courier", 24, "normal"))
        
        
    def pointsManager(self,p1pm,p2pm,pen):
        pressedKey = keyboard.read_key()
        if pressedKey == ArrowsP1[self.currentDirection].value and not(str(pen.shape())=="assets/clear.gif"):
            self.blank()
            self.player1GotPoint(p1pm)
            self.spamDetection()
            self.randomizer()
        elif pressedKey == ArrowsP2[self.currentDirection].value and not(str(pen.shape())=="assets/clear.gif"):
            self.player2GotPoint(p2pm)
            self.blank()
            self.spamDetection()
            self.randomizer()    
    
    def spamDetection(self):
        passedTime = 0
        print("before loop")
        random_delay = random.uniform(0.2, 2.5)
        print("the delay is "+str(random_delay))
        t = time.time()
        while(passedTime <= random_delay):
            #spam detection so if key is pressed add to counter and if it reaches 5 activate the pump
            if keyboard.is_pressed("w")or keyboard.is_pressed("a")or keyboard.is_pressed("s")or keyboard.is_pressed("d"):
                self.spamP2 +=1
                print("P2 BOZO")
                if(self.spamP2==5):
                    self.spamP2 =0
                    print("PUMP ON P1")
            if keyboard.is_pressed("up")or keyboard.is_pressed("down")or keyboard.is_pressed("right")or keyboard.is_pressed("left"):
                self.spamP1 +=1
                print("P1 BOZO")
                if(self.spamP1==5):
                    self.spamP1 =0
                    print("PUMP ON P1")                        
            passedTime = time.time() - t    
        print("boop")          
                      
class scoreWriter: #Responsible for writing score to screen
    def __init__(self,scoreP1,scoreP2) -> None:
        self.scoreP1 = scoreP1
        self.scoreP2 =scoreP2
        