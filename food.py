from turtle import Turtle
import random

SHAPE = "circle"
FRUIT_COLOR = "red"

SPECIAL_SHAPE = "turtle"
TURTLE_COLOR = "DarkOliveGreen1"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        random_number = random.randint(1, 10)
        self.set_food(random_number)
        self.setheading(90)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_random_number = random.randint(1, 10)
        self.set_food(new_random_number)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def set_food(self, num):
        if num == 1:
            self.shape(SPECIAL_SHAPE)
            self.color(TURTLE_COLOR)
            self.name = "turtle"
        else:
            self.shape(SHAPE)
            self.color(FRUIT_COLOR)
            self.name = "fruit"
