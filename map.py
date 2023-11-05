from cmu_graphics import *
import random
from usefulFunctions import *


class Flag:
    def __init__(self, app, pos):
        self.height = 100
        self.width = 100
        self.pos = pos
        self.captured = False

    def checkCollision(self, player):
        return collisionBetweenTwoRects(
            self.pos,
            self.width,
            self.height,
            player.pos,
            player.size,
            player.size,
        )

    def display(self):
        if self.captured:
            drawImage(
                app.imageDict["oyster"],
                self.pos[0],
                self.pos[1],
                align="center",
                width=self.width,
                height=self.height,
            )
        else:
            drawImage(
                app.imageDict["oyster-pearl"],
                self.pos[0],
                self.pos[1],
                align="center",
                width=self.width,
                height=self.height,
            )


class Seaweed:
    def __init__(self, pos):
        self.pos = pos
        factor = random.random() / 2 + 0.5
        self.width = 100 * factor
        self.height = 200 * factor

    def checkCollision(self, player):
        return collisionBetweenTwoRects(
            self.pos,
            self.width,
            self.height,
            player.pos,
            player.size,
            player.size,
        )

    def display(self):
        drawImage(
            app.imageDict["seaweed"],
            self.pos[0],
            self.pos[1],
            align="center",
            width=self.width,
            height=self.height,
        )


class Rock:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def checkCollision(self, otherPos, otherR):
        return collisionBetweenTwoCircles(self.pos, self.radius, otherPos, otherR)

    def pushPlayerOut(self, player):
        nVector = pushOutDir(self.pos, player.pos)
        totalRadius = self.radius + player.size / 2
        # change player position to be just outside rock
        player.pos = [
            self.pos[0] + totalRadius * nVector[0],
            self.pos[1] + totalRadius * nVector[1],
        ]

    def display(self):
        drawImage(
            app.imageDict["rock"],
            self.pos[0],
            self.pos[1],
            align="center",
            width=self.radius * 2,
            height=self.radius * 2,
        )
        # drawCircle(self.pos[0], self.pos[1], self.radius)


def createObstacles(app):
    createRocks(app)
    createSeaweed(app)


def createRocks(app):
    app.rocks = []
    for _ in range(random.randint(5, 7)):
        xVal = random.randrange(app.width - app.margin * 8) + app.margin * 4
        yVal = (
            random.randrange(app.fieldCanvas["height"] - app.margin * 2)
            + app.fieldCanvas["topLeftY"]
            + app.margin
        )
        radius = random.randrange(50) + 25
        app.rocks.append(Rock((xVal, yVal), radius))


def createSeaweed(app):
    app.seaweeds = []
    for _ in range(random.randint(2, 5)):
        xVal = random.randrange(app.width - app.margin * 8) + app.margin * 4
        yVal = (
            random.randrange(app.fieldCanvas["height"] - app.margin * 2)
            + app.fieldCanvas["topLeftY"]
            + app.margin
        )
        app.seaweeds.append(Seaweed((xVal, yVal)))
