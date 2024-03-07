from turtle import Turtle
from random import choice
import time
COLORS=["red","pink","blue","black","yellow","green"]
class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color(choice(COLORS))
        self.penup()
        self.goto(x=0,y=-280)
    def move(self):
        self.forward(10)
    def reset_position(self):
        time.sleep(0.5)
        self.goto(x=0, y=-280)






