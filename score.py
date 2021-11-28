from turtle import Turtle, Screen
import csv

screen = Screen()


FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player_name = screen.textinput(title="Game start", prompt="Insert your name.")
        self.penup()
        self.hideturtle()
        self.life = 0
        self.score = 0
        self.goto(-300, -290)
        self.color("white")
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def increase_score(self):
        self.score += 50
        self.clear()
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def decrease_life(self):
        self.life -= 1
        self.clear()
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def save_score(self):
        high_score = [self.player_name, self.score]
        with open("score", "a") as file:
            write = csv.writer(file)
            write.writerow(high_score)
