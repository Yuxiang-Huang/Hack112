from cmu_graphics import *

from test import *


class Player:
    def __init__(self):
        self.pos = [400, 400]
        self.size = 100
        self.speed = 10
        self.movementDirections = [False] * 4

    def update(self):
        # up
        if self.movementDirections[0]:
            self.pos[1] -= self.speed
        # left
        if self.movementDirections[1]:
            self.pos[0] -= self.speed
        # down
        if self.movementDirections[2]:
            self.pos[1] += self.speed
        # right
        if self.movementDirections[3]:
            self.pos[0] += self.speed


def onAppStart(app):
    app.p1 = Player()
    app.p2 = Player()
    app.paused = False


def redrawAll(app):
    drawCharacter(app.p1)


def drawCharacter(player):
    drawRect(player.pos[0], player.pos[1], player.size, player.size)


def onKeyPress(app, key):
    if "w" in key:
        app.p1.movementDirections[0] = True
    if "a" in key:
        app.p1.movementDirections[1] = True
    if "s" in key:
        app.p1.movementDirections[2] = True
    if "d" in key:
        app.p1.movementDirections[3] = True


def onKeyRelease(app, key):
    if "w" in key:
        app.p1.movementDirections[0] = False
    if "a" in key:
        app.p1.movementDirections[1] = False
    if "s" in key:
        app.p1.movementDirections[2] = False
    if "d" in key:
        app.p1.movementDirections[3] = False


def onStep(app):
    if not app.paused:
        takeStep(app)


def takeStep(app):
    app.p1.update()


def main():
    runApp(1200, 700)


main()
