from gpiozero import Button



class PlayerController:
    def __init__(self,upPin,downPin,leftPin,rightPin):
        
        self.upPin = upPin
        self.downPin = downPin
        self.leftPin = leftPin
        self.rightPin = rightPin
        
        self.pinArray =[self.upPin,self.downPin,self.rightPin,self.leftPin]
        self.upButton = Button(upPin)
        self.downButton = Button(downPin)
        self.leftButton = Button(leftPin)
        self.rightButton = Button(rightPin)
        self.ButtonArray =[self.upButton,self.downButton,self.rightButton,self.rightButton]
        print("Player Controller Activated")
    