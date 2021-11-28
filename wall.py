from turtle import Turtle

walls = []


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.create_block()
        self.walls = walls

    def create_block(self):
        global walls
        walls = []
        for x in range(1, 6):
            y_pos = -155
            for _ in range(1, 6):
                x_pos = -505 + (x * 155)
                for _ in range(1, 6):
                    block = Turtle()
                    block.shape("square")
                    block.color("white")
                    block.penup()
                    block.goto(x_pos, y_pos)
                    walls.append(block)
                    x_pos += 23
                y_pos += 23
