from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height, move_distance):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.md = move_distance
        self.score = 0
        self.setpos(- screen_width / 2 + 2 * self.md, screen_height / 2 - 2 * self.md)
        self.write(f"Your score: {self.score}", font=('Arial', self.md, 'normal'), align="left")

    def scored(self):
        self.clear()
        self.score += 1
        self.write(f"Your score: {self.score}", font=('Arial', self.md, 'normal'), align="left")

    def reset_score(self):
        pass