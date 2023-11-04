from cmu_graphics import *


class Player:
    def __init__(self, moveKeys, color, spawnPosition):
        self.pos = [spawnPosition[0], spawnPosition[1]]
        self.color = color
        self.spawnPosition = spawnPosition
        self.size = 50
        self.speed = 10
        self.moveKeys = moveKeys
        self.moveDirections = [False, False, False, False]

    def display(self):
        drawRect(
            self.pos[0],
            self.pos[1],
            self.size,
            self.size,
            fill=self.color,
            align="center",
        )

    def update(self, app):
        # up
        if self.moveDirections[0]:
            self.pos[1] -= self.speed
        # left
        if self.moveDirections[1]:
            self.pos[0] -= self.speed
        # down
        if self.moveDirections[2]:
            self.pos[1] += self.speed
        # right
        if self.moveDirections[3]:
            self.pos[0] += self.speed

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

        # obstacle check
        for rock in app.rocks:
            if rock.checkCollision(self.pos, self.size / 2):
                rock.pushPlayerOut(self)

    # def boundaryCheck(self, app):
    #     if self.pos[0] < +self.size / 2:
    #         return False
    #     if self.pos[0] > app.width - self.size / 2:
    #         return False
    #     if self.pos[1] < app.fieldCanvas["topLeftY"] + self.size / 2:
    #         return False
    #     if (
    #         self.pos[1]
    #         > app.fieldCanvas["topLeftY"] + app.fieldCanvas["height"] - self.size / 2
    #     ):
    #         return False

    def updateDirection(self, key, boolean):
        if self.moveKeys[0] in key:
            self.moveDirections[0] = boolean
        if self.moveKeys[1] in key:
            self.moveDirections[1] = boolean
        if self.moveKeys[2] in key:
            self.moveDirections[2] = boolean
        if self.moveKeys[3] in key:
            self.moveDirections[3] = boolean

    def respawn(self):
        self.pos = [self.spawnPosition[0], self.spawnPosition[1]]
