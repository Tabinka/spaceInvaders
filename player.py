from turtle import Turtle, Screen
import os

screen = Screen()
image = os.path.expanduser("player.gif")
screen.addshape('player.gif')


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.player = Turtle()
        self.shoot = False
        self.createPlayer()

    def createPlayer(self):
        self.player.shape(image)
        self.player.penup()
        self.player.goto(0, -250)

    def createShoot(self):
        if not self.shoot or self.shoot.ycor() > 300:
            screen.tracer(0)
            self.shoot = Turtle()
            self.shoot.shape("square")
            self.shoot.penup()
            self.shoot.shapesize(1, .1)
            self.shoot.goto(self.player.xcor(), self.player.ycor())
            self.shoot.color("green")

    def shooting(self):
        new_y = self.shoot.ycor() + 13
        self.shoot.goto(self.shoot.xcor(), new_y)

    def move_left(self):
        new_x = self.player.xcor() - 13
        self.player.goto(new_x, self.player.ycor())

    def move_right(self):
        new_x = self.player.xcor() + 13
        self.player.goto(new_x, self.player.ycor())
