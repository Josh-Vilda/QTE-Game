from round import Round

class guessingScore:
    gameWon = False

    def __init__(self):
        self.score = 0

    def set_score(self):
            self.score += 1

    def get_score(self):
            return self.score