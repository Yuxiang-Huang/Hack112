from cmu_graphics import *
import random


class Flag:
    def __init__(self, app, pos):
        self.flagHeight = 100
        self.flagWidth = 50
        self.pos = pos

    def display(self):
        drawRect(
            self.pos[0],
            self.pos[1],
            self.flagWidth,
            self.flagHeight,
            fill="red",
            align="center",
        )


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
        xVal = random.randrange(app.width - app.margin * 4) + app.margin * 2
        yVal = (
            random.randrange(app.fieldCanvas["height"] - app.margin * 2)
            + app.fieldCanvas["topLeftY"]
            + app.margin
        )
        width = random.randrange(50) + 25
        height = random.randrange(50) + 25
        app.obstacles.append(Obstacle((xVal, yVal), width, height))
