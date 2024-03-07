from turtle import Turtle

INC=1
class Level(Turtle):
    def __init__(self):
        self.level_num=1

        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-350,y=250)
        self.write(f"LEVEL:{self.level_num}",align="left",font=("Courier",20,"normal"))
    def increment(self):
        self.clear()
        self.level_num+=1
        self.write(f"LEVEL:{self.level_num}", align="left", font=("Courier", 20, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",40,"normal"))





