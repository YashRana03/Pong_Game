from turtle import Turtle


# Ball class creates the ball object
class Ball(Turtle):
    # Creates the ball from a turtle object
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.speed("slowest")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.num = 0
        self.sleep = 0.05

    # Moves the ball in the forward direction
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Makes the ball bounce of the top and bottom edges
    def bounce(self):
        self.y_move *= -1

    # Inverts the x-direction of the ball to the left
    def r_paddle_bounce(self):
        self.x_move = -abs(self.x_move)

    # Inverts the x-direction of the ball to the right
    def l_paddle_bounce(self):
        self.x_move = abs(self.x_move)

    # Increases the speed of the ball
    def increase_speed(self):
        if not self.sleep < 0.03:
            self.sleep -= 0.003

    # Resets the speed of the ball and takes it to the starting position
    def reset(self):
        self.x_move *= 1
        self.goto(0, 0)
        self.sleep = 0.05










