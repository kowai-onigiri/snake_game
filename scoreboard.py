from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier New', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self, point):
        self.score += point
        self.clear()
        self.update()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
