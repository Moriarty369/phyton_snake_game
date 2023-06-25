import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
# evitamos que se pixele snake al avanzar (apagando el trazer bool)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    # Detectando colisiones con food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detectando colisiones con las paredes
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        is_game_on = False
        scoreboard.game_over()

    # Detectando colisiones con la propia serpiente
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()