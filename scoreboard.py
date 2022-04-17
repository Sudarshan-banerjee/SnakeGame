from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-30, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'score: {self.score}', move=False, font=('arial', 15, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(-50, 0)
        self.write('GAME OVER :(', font=('arial', 15, 'normal'))

