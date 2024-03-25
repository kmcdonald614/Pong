from turtle import Turtle


# creates a new scoreboard with the score being 0-0.Giving the scoreboard the color of white.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    # updates the scoreboard by first clearing the current scoreboard, moves the cursor(without writing)
    # to the appropriate spot to update the scores, then rewriting the new scores.
    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    # add a point to the left player.
    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    # add a point to the right player.
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    # when right player wins, congratulate them.
    def right_wins(self):
        self.goto(x=0, y=0)
        self.write("Right Player Wins!", align="center", font=("Courier", 30, "normal"))

    # when left player wins, congratulate them.
    def left_wins(self):
        self.goto(x=0, y=0)
        self.write("Left Player Wins!", align="center", font=("Courier", 30, "normal"))
