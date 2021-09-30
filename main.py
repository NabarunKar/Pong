from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()


screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
# making the paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

screen.tracer(0)  # ignore animations

# moving paddle
screen.listen()  # listening for keystrokes
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()