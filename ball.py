from turtle import Turtle

# creates a white ball that has a diagonal movement and starts at a slow speed.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    # moves the ball in a diagonal direction at the beginning of the game.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    # when ball hits the wall(ceiling) increase speed of ball and change direction of ball to be mirrored.
    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    # when ball hits other paddle, the ball is sent the direction of the other player and ball speeds up.
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    # after each point is scored, the ball is put in the center again, this time the person who did not
    # serve last time would be "serving".
    def reset_position(self):
        self.ball_speed = 0.1
        self.goto(x=0, y=0)
        self.bounce_x()
