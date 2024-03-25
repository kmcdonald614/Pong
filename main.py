from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen() # creates a black screen with a title "Pong"
screen.bgcolor("black")
screen.setup(width=800, height=600) # set up the screen with a size of 800 x 600.
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0)) # puts the paddle in the middle of the screen on the right side.
left_paddle = Paddle((-350, 0)) # same for left.
ball = Ball()
scoreboard = Scoreboard()


screen.listen() # has the screen "listen" for a keystroke.
screen.onkey(right_paddle.go_up, "Up") # the right player pushes up arrow to move up and down arrow to move down.
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w") # the left player pushes w to move up and s to move down.
screen.onkey(left_paddle.go_down, "s")


# while the game is still being played( no one has quit or gotten a score of 10), continue playing.
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed) # To maintain the speed of the ball
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if ball goes past the right paddle abd if so, left player scores point.
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.left_point()

    #Detect if the ball goes past the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    # If left or right player gets to 10 points, the game is over.
    if scoreboard.left_score == 10:
        game_is_on = False
        scoreboard.left_wins()
    elif scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.right_wins()

screen.exitonclick()
