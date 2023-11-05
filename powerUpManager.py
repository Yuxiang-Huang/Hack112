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
        app.powerUps.append(Freeze(randomPos))
    # elif choice == 1:
    #     app.powerUps.append((randomPos))


def collideWithAnyRock(app, pos):
    for rock in app.rocks:
        if rock.checkCollision(pos, app.powerUpSize):
            return True
    return False


class PowerUp:
    def display(self, app, imageName):
        drawImage(
            app.imageDict[imageName],
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

    def display(self, app):
        PowerUp.display(self, app, "freeze")

    def use(self, app, player):
        if player == app.p1:
            app.p2.freeze(app)
        else:
            app.p1.freeze(app)
