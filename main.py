from timmy import Timmy
from turtle import Turtle,Screen
from cars import Cars
from level import Level
import time
screen=Screen()
screen.tracer(0)
timmy=Timmy()

level=Level()
cars=Cars()
screen.setup(height=600,width=800)
screen.listen()
screen.onkey(key="Up",fun=timmy.move)

is_game=True
cars_mo=True
while is_game:
    time.sleep(0.1)
    screen.update()
    cars.creat_car()
    cars.move_cars()
    if timmy.ycor()==290:
        level.increment()
        timmy.reset_position()
        cars.speed()
    for i in cars.all_cars:
        if timmy.distance(i)<20:
            level.game_over()
            is_game=False









screen.exitonclick()