from cmu_graphics import *
import random
from usefulFunctions import *


def updateSpawnPowerUp(app):
    if len(app.powerUps) == 0:
        app.timeUntilSpawn -= 1
    if app.timeUntilSpawn == 0:
        spawnPowerUp(app)
        app.timeUntilSpawn = app.powerUpSpawnTime


def spawnPowerUp(app):
    # determine a random position that does not collide with a rock
    randomY = random.randrange(app.fieldCanvas["height"]) + app.fieldCanvas["topLeftY"]
    randomPos = (app.width / 2, randomY)
    while collideWithAnyRock(app, randomPos):
        randomY = (
            random.randrange(app.fieldCanvas["height"]) + app.fieldCanvas["topLeftY"]
        )
        randomPos = (app.width / 2, randomY)

    choice = random.randint(0, 5)
    if choice == 0:
        app.powerUps.append(Mine(randomPos))
    elif choice == 1:
        app.powerUps.append(Time(randomPos))
    elif choice == 2:
        app.powerUps.append(Teleport(randomPos))
    elif choice == 3:
        app.powerUps.append(Speed(randomPos))
    elif choice == 4:
        app.powerUps.append(PushAway(randomPos))
    elif choice == 5:
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

    def use(self, app, player):
        if player == app.p1:
            app.p2.freeze(app.stepsPerSecond)  # freeze time
        else:
            app.p1.freeze(app.stepsPerSecond)  # freeze time


class PushAway(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "pushAway"
        self.pushAwayConstant = 150  # dist divide by pushAwayConstant = seconds to be pushed with a max of 2 and min of 0.5
        self.pushAwayMaxStrength = 15
        self.pushAwayMinStrength = 5

    def use(self, app, player):
        if player == app.p1:
            other = app.p2
        else:
            other = app.p1
        pushDir = pushOutDir(player.pos, other.pos)
        dist = distance(other.pos[0], other.pos[1], player.pos[0], player.pos[1])
        pushTime = max(min(1.5, self.pushAwayConstant / dist), 0.5) * app.stepsPerSecond
        print(pushTime)
        other.pushAway(
            pushDir,
            self.pushAwayMaxStrength,
            (self.pushAwayMaxStrength - self.pushAwayMinStrength) / pushTime,
            pushTime,
        )


class Speed(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "bootWithWings"

    def use(self, app, player):
        player.speedUp(app.stepsPerSecond * 2)  # speed up time


class Teleport(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "teleport"
        self.teleportDist = 300
        self.teleportedAnimationTime = 30

    def use(self, app, player):
        player.teleport(self.teleportDist, self.teleportedAnimationTime)


class Time(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "clock"
        self.secondsBefore = 5

    def use(self, app, player):
        player.timeTravel(
            self.secondsBefore * app.stepsPerSecond,
            app.stepsPerSecond,
        )


class Mine(PowerUp):
    def __init__(self, pos):
        self.pos = pos
        self.name = "mine"

    def use(self, app, player):
        player.putMine()
