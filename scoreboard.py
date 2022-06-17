from turtle import  Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open ('../../../Desktop/data.txt','r') as file:
            self.high_score=int(file.read())
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
            with open ('../../../Desktop/data.txt','w') as updated_file:
                updated_file.write(f'{self.high_score}')
        self.score=0
        self.update_score()

