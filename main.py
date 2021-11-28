import time
from turtle import Screen, Turtle
from player import Player
from enemy import Enemy
from wall import Wall
from score import Score

FONT = ("Courier", 18, "normal")

screen = Screen()
screen.tracer(0)
player = Player()
enemy = Enemy()
wall = Wall()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("black")
score = Score()
text = Turtle()
text.penup()
text.hideturtle()
text.goto(0, 0)
text.color("white")
visible_enemy = True


def distance():
    global visible_enemy
    y = 0
    for en in enemy.enemies:
        if en.isvisible():
            y += 1
            if en.distance(player.shoot) < 50:
                score.increase_score()
                player.shoot.goto(-2000, 2000)
                en.hideturtle()
    if y == 0:
        visible_enemy = False


def distance_wall(thing):
    for wal in wall.walls:
        if wal.distance(thing) < 10:
            thing.goto(-2000, 2000)
            wal.hideturtle()
            wal.goto(-1000, 1000)
            return False
    return True


game = True

screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.createShoot, "space")

screen.tracer(1)
x = 0
while game:
    time.sleep(.1)
    screen.update()
    if score.player_name is None:
        game = False
    if x % 56 == 0:
        enemy.bomb.reset()
        enemy.create_bomb()
    enemy.enemy_movement()
    enemy.bomb_movement()
    if player.shoot:
        player.shooting()
        distance()
        distance_wall(player.shoot)
    if player.player.distance(enemy.bomb) < 50:
        player.player.goto(0, player.player.ycor())
        if score.life > 0:
            score.decrease_life()
        else:
            score.save_score()
            game = False
        enemy.bomb.goto(-1000, 1000)
    elif not distance_wall(enemy.bomb):
        x = 0
    elif not visible_enemy:
        score.save_score()
        game = False
    x += 1

text.write(f"GAME OVER", align="center", font=FONT)
screen.exitonclick()
