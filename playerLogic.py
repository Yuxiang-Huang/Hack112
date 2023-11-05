from cmu_graphics import *
from usefulFunctions import *


class Player:
    def __init__(self, moveKeys, color, spawnPosition):
        self.pos = [spawnPosition[0], spawnPosition[1]]
        self.color = color
        self.hasFlag = False
        self.spawnPosition = spawnPosition
        self.size = 100
        self.speed = 10
        self.moveKeys = moveKeys
        self.moveDirections = [False, False, False, False]
        self.powerUp = None

    def display(self, app):
        if self.hasFlag:
            drawRect(
                self.pos[0],
                self.pos[1],
                self.size,
                self.size,
                fill="purple",
                align="center",
            )
        else:
            # drawRect(
            #     self.pos[0],
            #     self.pos[1],
            #     self.size,
            #     self.size,
            #     fill=self.color,
            #     align="center",
            # )
            if self == app.p1:
                drawImage(
                    app.imageDict["blueFish"],
                    self.pos[0],
                    self.pos[1],
                    align="center",
                    width=self.size,
                    height=self.size,
                )
            else:
                drawImage(
                    app.imageDict["redFish"],
                    self.pos[0],
                    self.pos[1],
                    align="center",
                    width=self.size,
                    height=self.size,
                )

    def update(self, app):
        curSpeed = self.speed
        for seaweed in app.seaweeds:
            if seaweed.checkCollision(self):
                curSpeed /= 2

        # up
        if self.moveDirections[0]:
            self.pos[1] -= curSpeed
        # left
        if self.moveDirections[1]:
            self.pos[0] -= curSpeed
        # down
        if self.moveDirections[2]:
            self.pos[1] += curSpeed
        # right
        if self.moveDirections[3]:
            self.pos[0] += curSpeed

        # boundary check
        self.pos[0] = max(0 + self.size / 2, self.pos[0])
        self.pos[0] = min(
            app.width - self.size / 2,
            self.pos[0],
        )
        self.pos[1] = max(app.fieldCanvas["topLeftY"] + self.size / 2, self.pos[1])
        self.pos[1] = min(
            app.fieldCanvas["topLeftY"] + app.fieldCanvas["height"] - self.size / 2,
            self.pos[1],
        )

        # rock obstacle check
        for rock in app.rocks:
            if rock.checkCollision(self.pos, self.size / 2):
                rock.pushPlayerOut(self)

        # check to get power up
        index = len(app.powerUps) - 1
        while index >= 0:
            if collisionBetweenTwoRects(
                self.pos,
                self.size,
                self.size,
                app.powerUps[index].pos,
                app.powerUpSize,
                app.powerUpSize,
            ):
                self.powerUp = app.powerUps[index]
                app.powerUps.pop(index)
            index -= 1

    def updateDirection(self, key, boolean):
        if self.moveKeys[0] in key:
            self.moveDirections[0] = boolean
        if self.moveKeys[1] in key:
            self.moveDirections[1] = boolean
        if self.moveKeys[2] in key:
            self.moveDirections[2] = boolean
        if self.moveKeys[3] in key:
            self.moveDirections[3] = boolean

    def respawn(self, otherFlag):
        self.pos = [self.spawnPosition[0], self.spawnPosition[1]]
        if self.hasFlag:
            self.hasFlag = False
            otherFlag.captured = False
