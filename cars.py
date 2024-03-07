from turtle import Turtle
from random import randint,choice
CARS_COLORS=["#747264","#561C24","#85586F","#294B29","#720455","#D24545","#D63484","#FFDD95"]
STARTING_SPEED=5
INCREMENT=5

class Cars():
    def __init__(self):
        super().__init__()
        self.car_speed=STARTING_SPEED
        self.all_cars=[]
    def creat_car(self):
        num=randint(1,6)
        if num==6:
            new_car=Turtle()
            new_car.shape("square")
            new_car.resizemode("user")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(choice(CARS_COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=400,y=randint(-250,280))
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.forward(self.car_speed)
    def speed(self):
        self.car_speed+=INCREMENT
        self.move_cars()










