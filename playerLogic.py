from cmu_graphics import *


class Player:
    def __init__(self, moveKeys):
        self.pos = [400, 400]
        self.size = 100
        self.speed = 10
        self.moveKeys = moveKeys
        self.moveDirections = [False, False, False, False]

    def drawCharacter(self):
        drawRect(self.pos[0], self.pos[1], self.size, self.size)

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
        print(key)

        if self.moveKeys[0] in key:
            self.moveDirections[0] = boolean
        if self.moveKeys[1] in key:
            self.moveDirections[1] = boolean
        if self.moveKeys[2] in key:
            self.moveDirections[2] = boolean
        if self.moveKeys[3] in key:
            self.moveDirections[3] = boolean
