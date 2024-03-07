from turtle import Turtle, Screen
import random
import time
from cars import Cars
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20
# NUMBER_CARS = 10

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue", "yellow")
turtle.penup()
turtle.setheading(90)
turtle.setpos(0, - int(SCREEN_HEIGHT/2) + MOVE_DISTANCE)

cars = Cars(SCREEN_WIDTH, SCREEN_HEIGHT, MOVE_DISTANCE)

scoreboard = ScoreBoard(SCREEN_WIDTH, SCREEN_HEIGHT, MOVE_DISTANCE)


def move_turtle():
    turtle.forward(MOVE_DISTANCE)

def over_street():
    if turtle.ycor() >= SCREEN_HEIGHT / 2:
        turtle.sety(- int(SCREEN_HEIGHT/2) + MOVE_DISTANCE)
        return True
    else:
        return False


game_running = True


def quit_game():
    global game_running
    game_running = False
    sign = Turtle()
    sign.color("black")
    sign.penup()
    sign.hideturtle()
    sign.score = 0
    sign.setpos(0, 0)
    sign.write(f"GAME OVER", font=('Arial', 2 * MOVE_DISTANCE, 'normal'), align="center")


time.sleep(0.1)
screen.update()

screen.listen()
screen.onkey(quit_game, "space")
screen.onkey(move_turtle, "Up")

while game_running:
    crossed = over_street()
    if crossed:
        scoreboard.scored()
        cars.speed_up()
    collided = cars.collision(turtle)
    if collided:
        quit_game()
    cars.move()
    cars.reposition()
    time.sleep(0.1/(scoreboard.score + 1))
    screen.update()

screen.exitonclick()