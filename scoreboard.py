from turtle import Turtle


# ScoreBoard class creates the scoreboard object
class ScoreBoard(Turtle):
    # Creates the scoreboard from a turtle object
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    # Updates the scoreboard on the screen
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Increases the score of the left player
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Increases the score of the right player
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
