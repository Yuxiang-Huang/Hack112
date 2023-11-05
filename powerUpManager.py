from cmu_graphics import *
import random
from usefulFunctions import *


def updateSpawnPowerUp(app):
    if len(app.powerUps) == 0:
        app.timeUntilSpawn -= 1
    if app.timeUntilSpawn == 0:
        spawnPowerUp(app)
        app.timeUntilSpawn = 150


def spawnPowerUp(app):
    # determine a random position that does not collide with a rock
    randomY = random.randrange(app.fieldCanvas["height"]) + app.fieldCanvas["topLeftY"]
    randomPos = (app.width / 2, randomY)
    while collideWithAnyRock(app, randomPos):
        randomY = (
            random.randrange(app.fieldCanvas["height"]) + app.fieldCanvas["topLeftY"]
        )
        randomPos = (app.width / 2, randomY)

    choice = random.randint(0, 6)
    if choice >= 0:
        app.powerUps.append(PushAway(randomPos))
    elif choice == 1:
        app.powerUps.append(Freeze(randomPos))


def collideWithAnyRock(app, pos):
    for rock in app.rocks:
        if rock.checkCollision(pos, app.powerUpSize):
            return True
    return False


class PowerUp:
    def display(self, app):
        drawImage(
            app.imageDict[self.name],
            self.pos[0],
            self.pos[1],
            align="center",
            width=app.powerUpSize,
            height=app.powerUpSize,
        )

    def checkCollision(self, player, app):
        return collisionBetweenTwoRects(
            player.pos,
            player.size,
            player.size,
            self.pos,
            app.powerUpSize,
            app.powerUpSize,
        )


class Freeze(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "freeze"

    def use(self, player):
        player.freeze(app.stepsPerSecond)  # freeze time


class PushAway(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "pushAway"
        self.pushAwayConstant = (
            50  # dist divide by pushAwayConstant = seconds to be pushed with a max of 2
        )
        self.pushAwayMaxStrength = 15
        self.pushAwayMinStrength = 5

    def use(self, app, player):
        dist = dist(self.pos[0], self.pos[1], player.pos[0], player.pos[1])
        pushTime = min(2, self.pushAwayConstant / dist) * app.stepsPerSecond
        pushDir = pushOutDir(self.pos, player)
        player.pushAway(
            pushDir,
            pushTime,
            self.pushAwayMaxStrength,
            (self.pushAwayMaxStrength - self.pushAwayMinStrength) / pushTime,
            pushTime,
        )
