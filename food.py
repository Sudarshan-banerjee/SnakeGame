from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.penup()
        self.refresh()
        self.speed('fastest')

    def refresh(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)