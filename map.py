from cmu_graphics import *
import random


class Flag:
    def __init__(self, app, pos):
        self.height = 100
        self.width = 50
        self.pos = pos
        self.captured = False

    def checkCollision(self, player):
        if abs(self.pos[0] - player.pos[0]) < self.width / 2 + player.size / 2:
            if abs(self.pos[1] - player.pos[1]) < self.height / 2 + player.size / 2:
                return True
        return False

    def display(self):
        if self.captured:
            drawRect(
                self.pos[0],
                self.pos[1],
                self.width,
                self.height,
                fill="purple",
                align="center",
            )
        else:
            drawRect(
                self.pos[0],
                self.pos[1],
                self.width,
                self.height,
                fill="red",
                align="center",
            )


class Seaweed:
    def __init__(self, pos):
        self.pos = pos
        self.width = 150
        self.height = 200

    def checkCollision(self, player):
        if abs(self.pos[0] - player.pos[0]) < self.width / 2 + player.size / 2:
            if abs(self.pos[1] - player.pos[1]) < self.height / 2 + player.size / 2:
                return True
        return False

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
        return (
            (self.pos[0] - otherPos[0]) ** 2 + (self.pos[1] - otherPos[1]) ** 2
        ) ** 0.5 < self.radius + otherR

    def pushPlayerOut(self, player):
        # find normalized vector
        nVector = [player.pos[0] - self.pos[0], player.pos[1] - self.pos[1]]
        mag = (
            (self.pos[0] - player.pos[0]) ** 2 + (self.pos[1] - player.pos[1]) ** 2
        ) ** 0.5
        nVector = [nVector[0] / mag, nVector[1] / mag]
        # change player position to be just outside the rock
        player.pos = [
            self.pos[0] + (self.radius + player.size / 2) * nVector[0],
            self.pos[1] + (self.radius + player.size / 2) * nVector[1],
        ]

    def display(self):
        # drawImage(
        #     app.imageDict["rock"],
        #     self.pos[0],
        #     self.pos[1],
        #     align="center",
        #     width=self.radius * 2,
        #     height=self.radius * 2,
        # )
        drawCircle(self.pos[0], self.pos[1], self.radius)


def createObstacles(app):
    createRocks(app)
    createSeaweed(app)


def createRocks(app):
    app.rocks = []
    for _ in range(random.randrange(5) + 5):
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
    for _ in range(random.randrange(5) + 5):
        xVal = random.randrange(app.width - app.margin * 8) + app.margin * 4
        yVal = (
            random.randrange(app.fieldCanvas["height"] - app.margin * 2)
            + app.fieldCanvas["topLeftY"]
            + app.margin
        )
        app.seaweeds.append(Seaweed((xVal, yVal)))
