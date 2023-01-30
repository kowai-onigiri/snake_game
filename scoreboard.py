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
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self, point):
        self.score += point
        self.clear()
        self.update()


    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
