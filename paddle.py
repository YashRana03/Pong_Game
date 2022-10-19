from turtle import Turtle


# Paddle class creates the paddle object
class Paddle(Turtle):
    # Creates the paddle from a turtle object
    def __init__(self, initial_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(initial_position)

    # Moves the paddle upwards
    def move_up(self):
        if self. ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    # Moves the paddle downwards
    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)


