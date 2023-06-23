import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
# evitamos que se pixele snake al avanzar (apagando el trazer bool)
screen.tracer(0)

snake = Snake()

# Inputs controllers
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    # Controlamos la velocidad
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
