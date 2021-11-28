import random
from turtle import Turtle, Screen
import os

screen = Screen()
image = os.path.expanduser("enemy.gif")
screen.addshape('enemy.gif')
enemies = []


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.bomb = Turtle()
        self.left = True
        self.y = 250
        self.create_enemy()
        self.enemies = enemies

    def create_enemy(self):
        global enemies
        for _ in range(0, 2):
            x = 0
            for _ in range(0, 4):
                enemy = Turtle()
                enemy.shape(image)
                enemy.penup()
                enemy.goto(x, self.y)
                enemies.append(enemy)
                x -= 60
            self.y -= 60

    def create_bomb(self):
        self.bomb.shape("square")
        self.bomb.shapesize(1, .1)
        random_enemy = random.randint(0, len(enemies)-1)
        self.bomb.goto(enemies[random_enemy].xcor(), enemies[random_enemy].ycor())
        self.bomb.penup()
        self.bomb.color("white")

    def bomb_movement(self):
        new_y = self.bomb.ycor() - 13
        self.bomb.goto(self.bomb.xcor(), new_y)

    def enemy_movement(self):
        if self.left:
            if enemies[0].xcor() > -200:
                for en in enemies:
                    new_x = en.xcor() - 3
                    en.goto(new_x, en.ycor())
            else:
                for en in enemies:
                    new_y = en.ycor() - 3
                    en.goto(en.xcor(), new_y)
                self.left = False
        else:
            if enemies[0].xcor() < 300:
                for en in enemies:
                    new_x = en.xcor() + 3
                    en.goto(new_x, en.ycor())
            else:
                for en in enemies:
                    new_y = en.ycor() - 3
                    en.goto(en.xcor(), new_y)
                self.left = True
