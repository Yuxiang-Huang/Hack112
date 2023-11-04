from cmu_graphics import *


class Player:
    def __init__(self, moveKeys, color, spawnPosition):
        self.pos = [spawnPosition[0], spawnPosition[1]]
        self.color = color
        self.spawnPosition = spawnPosition
        self.size = 100
        self.speed = 10
        self.moveKeys = moveKeys
        self.moveDirections = [False, False, False, False]

    def drawCharacter(self):
        drawRect(
            self.pos[0],
            self.pos[1],
            self.size,
            self.size,
            fill=self.color,
            align="center",
        )

    def update(self):
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
