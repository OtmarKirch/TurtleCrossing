from turtle import Turtle
import random


def random_color():
    hex_value = "%06x" % random.randint(0, 0xFFFFFF)
    rand_color = "#" + hex_value
    return rand_color


class Cars(Turtle):
    def __init__(self, screen_width, screen_height, move_distance):
        super().__init__()
        self.carpark = []
        self.sw = screen_width
        self.sh = screen_height
        self.md = move_distance
        self.hideturtle()
        self.num_cars = int(screen_height / move_distance) - 3

        for i in range(0, self.num_cars):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(0.8, 2)
            car.setheading(180)
            car.color(random_color())
            car.sety(int(-self.sh/2 + 2 * self.md) + i * int(self.md * 1))
            x = -int(self.sw/2 - 2 * self.md)
            print(x)
            y = int(self.sw)
            car.setx(random.randint(x, y))
            car.speed(3)
            self.carpark.append(car)

    def move(self):
        for car in self.carpark:
            car.forward(car.speed())

    def reposition(self):
        for car in self.carpark:
            # same_pos_x = True
            # while same_pos_x:
            #     same_pos_x = False
            if car.xcor() <= - (self.sw / 2 + 2 * self.md):
                car.setx(random.randint(int(self.sw / 2 + self.md), int(self.sw / 2 + self.md + self.sw / 4)))
                i = random.randint(0, self.num_cars)
                car.sety(int(-self.sh / 2 + 2 * self.md) + i * int(self.md * 1))
                # for other_car in self.carpark:
                #     if other_car != car:
                #         if other_car.ycor() == car.ycor() and car.distance(other_car) < self.md * 2:
                #             same_pos_x = True

    def collision(self, turtle):
        collided = False
        for car in self.carpark:
            if car.distance(turtle) <= 30 and car.ycor() == turtle.ycor():
                print(car.pos())
                print(turtle.pos())
                collided = True
        return collided

    def speed_up(self):
        if self.carpark[0].speed() <= 10:
            for car in self.carpark:
                new_speed = car.speed()
                car.speed(new_speed)