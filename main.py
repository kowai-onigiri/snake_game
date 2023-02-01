import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

# ---------- SCREEN ----------
screen = Screen()

# --------- GAME FUNCTION -----------
play_again = True

food_choice = ["fruit", "turtle"]
random_choice = random.choice(food_choice)


def snake_game():
    # ---------- SCREEN SETUP ----------
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    # ---------- SCOREBOARD CREATION ----------
    scoreboard = Scoreboard()

    # ---------- SNAKE CREATION ----------
    snake = Snake()

    # ---------- FOOD CREATION ----------

    food = Food()

    # ---------- CONTROLS ----------
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # ---------- GAME ----------
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # --- detect collision with food ---
        if snake.head.distance(food) < 15:
            if food.name == "fruit":
                scoreboard.increase_score(1)
            else:
                scoreboard.increase_score(2)
            food.refresh()
            snake.extent()

        # --- detect collision with wall ---
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            scoreboard.reset_scoreboard()
            snake.reset()
            food.refresh()

        # --- detect collision with tail ---
        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_scoreboard()
                snake.reset()
                food.refresh()


snake_game()

# while play_again:
#     snake_game()
#     another_game = turtle.textinput("Snake Game", "Do you want to play again?").lower()
#     if another_game == "yes":
#         screen.clear()
#     else:
#         play_again = False

screen.exitonclick()
