from turtle import  Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f'Score :{self.score} Highest Score:{self.high_score}', align='center',font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f'Score :{self.score} Highest Score:{self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score=0
        self.update_score()

