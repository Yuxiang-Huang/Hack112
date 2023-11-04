from cmu_graphics import *
import random


class Obstacle:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

    def checkCollision(self, player):
        pass

    def display(self):
        drawRect(self.pos[0], self.pos[1], self.width, self.height)


def createObstacles(app):
    app.obstacles = []
    for i in range(random.randrange(5) + 5):
        xVal = random.randrange(100) + app.width
        yVal = random.randrange(200) + 100
        width = random.randrange(30) + 10
        height = random.randrange(30) + 10
        app.obstacles.append(Obstacle((xVal, yVal), width, height))
