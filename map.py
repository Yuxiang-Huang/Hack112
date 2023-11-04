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


# class Seaweed:
#     def __init__(self, pos, width, height):
#         self.pos = pos
#         self.width = width
#         self.height = height

#     def checkCollision(self, player):
#         # if collide horizontally
#         if abs(self.pos[0] - player.pos[0]) < self.width / 2 + player.size / 2:
#             # if collide vertically
#             if abs(self.pos[1] - player.pos[1]) < self.height / 2 + player.size / 2:
#                 return True

#     def display(self):
#         drawRect(self.pos[0], self.pos[1], self.width, self.height, align="center")


class Rock:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def checkCollision(self, player):
        # collision between player and rock
        if (
            (self.pos[0] - player.pos[0]) ** 2 + (self.pos[1] - player.pos[1]) ** 2
        ) ** 0.5 < self.radius + player.size / 2:
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
        drawCircle(self.pos[0], self.pos[1], self.radius)


def createRocks(app):
    app.rocks = []
    for i in range(random.randrange(5) + 5):
        xVal = random.randrange(app.width - app.margin * 4) + app.margin * 2
        yVal = (
            random.randrange(app.fieldCanvas["height"] - app.margin * 2)
            + app.fieldCanvas["topLeftY"]
            + app.margin
        )
        radius = random.randrange(50) + 25
        app.rocks.append(Rock((xVal, yVal), radius))
