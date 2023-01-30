from turtle import Turtle, Screen

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SNAKE_COLOR = "DarkSeaGreen3"
HEAD_COLOR = "DarkSeaGreen"

screen = Screen()


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.color(HEAD_COLOR)

    def create_snake(self):
        x = 0
        y = 0
        pos = (x, y)

        for num in range(3):
            self.add_segment(pos)
            x -= 20

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color(SNAKE_COLOR)
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def extent(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):

        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

