from cmu_graphics import *
from usefulFunctions import *
import random


class Player:
    def __init__(self, moveKeys, powerUpKey, color, spawnPosition):
        self.pos = [spawnPosition[0], spawnPosition[1]]
        self.color = color
        self.hasFlag = False
        self.spawnPosition = spawnPosition
        self.size = 75
        self.speed = 10
        self.score = 0

        # AR Values to draw movement tractor
        self.ARVals = [0, 0]

        # keys and movement
        self.moveKeys = moveKeys
        self.powerUpKey = powerUpKey
        self.moveDirections = [False, False, False, False]

        # power up variables
        self.powerUpName = None
        self.powerUp = None
        self.powerUpCoolDown = 0

        # freeze power up
        self.frozen = False
        self.freezeTime = 0

        # push away power up
        self.beingPushed = False
        self.pushDir = (0, 0)
        self.pushStrength = 0
        self.pushStrengthChange = 0
        self.pushTime = 0

        # speed power up
        self.speedy = False
        self.speedUptime = 0

        # teleport power up
        self.teleported = False
        self.teleportedAnimationTime = 0
        self.teleportFromPosition = (0, 0)
        self.teleportToPosition = (0, 0)

        # time travel power up
        self.timeTravelling = False
        self.timeTravelInterval = 0
        self.pastPositions = []
        self.count = 0

        # mine power up
        self.mines = []

    def display(self, app):
        if self == app.p1:
            if self.frozen:
                self.drawImageHelper("frozenBlueFish")
            elif self.speedy:
                self.drawImageHelper("blueFishWind")
            else:
                if self.hasFlag:
                    self.drawImageHelper("blueFishPearl")
                else:
                    self.drawImageHelper("blueFish")
        else:
            if self.frozen:
                self.drawImageHelper("frozenRedFish")
            elif self.speedy:
                self.drawImageHelper("redFishWind")
            else:
                if self.hasFlag:
                    self.drawImageHelper("redFishPearl")
                else:
                    self.drawImageHelper("redFish")

        # draw hand on fish if being pushed
        if self.beingPushed:
            self.drawImageHelper("pushAway")

        # draw clock on fish if time travelling
        if self.timeTravelling:
            self.drawImageHelper("clock")

        # teleport animation
        if self.teleported:
            self.teleportedAnimationTime -= 1
            if self.teleportedAnimationTime <= 0:
                self.teleported = False
            drawImage(
                app.imageDict["teleport"],
                self.teleportFromPosition[0],
                self.teleportFromPosition[1],
                align="center",
                width=self.size,
                height=self.size,
            )
            drawImage(
                app.imageDict["teleport"],
                self.teleportToPosition[0],
                self.teleportToPosition[1],
                align="center",
                width=self.size,
                height=self.size,
            )

        for mine in self.mines:
            drawImage(
                app.imageDict["mine"],
                mine[0],
                mine[1],
                align="center",
                width=self.size,
                height=self.size,
            )

    def drawImageHelper(self, nameOfImage):
        drawImage(
            app.imageDict[nameOfImage],
            self.pos[0],
            self.pos[1],
            align="center",
            width=self.size,
            height=self.size,
        )

    def update(self, app):
        # decrease power up cool down time
        self.powerUpCoolDown -= 1
        self.powerUpCoolDown = max(self.powerUpCoolDown, 0)

        # decrease push away time and strength
        if self.beingPushed:
            self.pushTime -= 1
            self.pos[0] += self.pushDir[0] * self.pushStrength
            self.pos[1] += self.pushDir[1] * self.pushStrength
            self.pushStrength -= self.pushStrengthChange
            if self.pushTime < 0:
                self.beingPushed = False

        # decrease freeze time until unfrozen
        if self.frozen:
            self.freezeTime -= 1
            if self.freezeTime < 0:
                self.frozen = False
            return

        # keep track of positions for time travelling
        self.count += 1
        if self.count % 15 == 0:
            self.pastPositions.append([self.pos[0], self.pos[1]])
            if len(self.pastPositions) > 10:
                self.pastPositions.pop(-1)

        # time travelling
        if self.timeTravelling:
            if self.count % self.timeTravelInterval == 0:
                if len(self.pastPositions) == 0:
                    self.timeTravelling = False
                else:
                    self.pos = self.pastPositions.pop(-1)

        # check if mine can kill opponent
        if self == app.p1:
            other = app.p2
            myFlag = app.flag1
        else:
            other = app.p1
            myFlag = app.flag2

        index = len(self.mines) - 1
        while index >= 0:
            mine = self.mines[index]
            if collisionBetweenTwoRects(
                mine, self.size, self.size, other.pos, other.size, other.size
            ):
                self.mines.pop(index)
                other.respawn(myFlag)
            index -= 1

        # movement
        curSpeed = self.speed

        # decrease speedup time
        if self.speedy:
            self.speedUptime -= 1
            curSpeed *= 2
            if self.speedUptime < 0:
                self.speedy = False

        # decrease speed if in seaweed (ignore if speedy)
        if not self.speedy:
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

        # check collision to get power up
        index = len(app.powerUps) - 1
        while index >= 0:
            if app.powerUps[index].checkCollision(self, app):
                self.powerUp = app.powerUps[index]
                self.powerUpName = app.powerUps[index].name
                self.powerUpCoolDown = 0
                app.powerUps.pop(index)
            index -= 1

    def updateDirection(self, keys, boolean):
        if self.moveKeys[0] in keys:
            self.moveDirections[0] = boolean
        if self.moveKeys[1] in keys:
            self.moveDirections[1] = boolean
        if self.moveKeys[2] in keys:
            self.moveDirections[2] = boolean
        if self.moveKeys[3] in keys:
            self.moveDirections[3] = boolean

    # region power ups usages
    def tryUsePowerUp(self, app, keys):
        if (
            self.powerUpKey in keys
            and self.powerUpCoolDown <= 0
            and self.powerUp != None
        ):
            self.powerUp.use(app, self)
            self.powerUpCoolDown = app.powerUpCoolDown

    def tryUsePowerUpARMode(self, app):
        if self.powerUpCoolDown <= 0 and self.powerUp != None:
            self.powerUp.use(app, self)
            self.powerUpCoolDown = app.powerUpCoolDown

    def freeze(self, freezeTime):
        self.frozen = True
        self.freezeTime = freezeTime

    def pushAway(self, pushDir, pushStrength, pushStrengthChange, pushTime):
        self.beingPushed = True
        self.pushDir = pushDir
        self.pushStrength = pushStrength
        self.pushStrengthChange = pushStrengthChange
        self.pushTime = pushTime

    def speedUp(self, speedUptime):
        self.speedy = True
        self.speedUptime = speedUptime

    def teleport(self, teleportDist, teleportedAnimationTime):
        vector = [0, 0]
        # up
        if self.moveDirections[0]:
            vector[1] -= 1
        # left
        if self.moveDirections[1]:
            vector[0] -= 1
        # down
        if self.moveDirections[2]:
            vector[1] += 1
        # right
        if self.moveDirections[3]:
            vector[0] += 1
        # random vector if not moving
        while vector[0] == 0 and vector[1] == 0:
            vector = [random.randint(-1, 1), random.randint(-1, 1)]
        # normalize
        vector = normalize(vector)

        # for animation
        self.teleported = True
        self.teleportedAnimationTime = teleportedAnimationTime
        self.teleportFromPosition = (self.pos[0], self.pos[1])

        # teleport
        self.pos[0] += vector[0] * teleportDist
        self.pos[1] += vector[1] * teleportDist

        self.teleportToPosition = (self.pos[0], self.pos[1])

    def timeTravel(self, stepsBefore, timeDuration):
        self.timeTravelling = True
        self.timeTravelInterval = stepsBefore / timeDuration

    def putMine(self):
        if len(self.mines) > 0:
            self.mines = []
        self.mines.append((self.pos[0], self.pos[1]))

    # endregion

    # region resets
    def respawn(self, otherFlag):
        self.resetPowerUp()
        self.pos = [self.spawnPosition[0], self.spawnPosition[1]]
        if self.hasFlag:
            self.hasFlag = False
            otherFlag.captured = False

    def resetPowerUp(self):
        self.powerUp = None
        self.powerUpCoolDown = 0

    def getPowerUp(self, other):
        self.powerUp = other.powerUp
        self.powerUpName = other.powerUpName
        self.powerUpCoolDown = 0

    # endregion


def displayTopBarP1(app):
    drawMovementTractor(app, app.p1, 25)
    drawLabel("P1 Score: " + str(app.p1.score), 150, app.topBarHeight / 2, size=16)
    drawRect(
        225,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        align="center",
        borderWidth=1,
        fill=None,
        border="black",
    )
    drawRect(
        275,
        app.topBarHeight / 2,
        200,
        app.topBarHeight / 2,
        align="left",
        borderWidth=1,
        fill=None,
        border="black",
    )
    if app.p1.powerUp != None:
        drawImage(
            app.imageDict[app.p1.powerUpName],
            225,
            app.topBarHeight / 2,
            align="center",
            width=app.topBarHeight / 2,
            height=app.topBarHeight / 2,
        )
        if app.p1.powerUpCoolDown != app.powerUpCoolDown:
            drawRect(
                275,
                app.topBarHeight / 2,
                200 * (1 - app.p1.powerUpCoolDown / app.powerUpCoolDown),
                app.topBarHeight / 2,
                borderWidth=1,
                align="left",
                fill="cyan",
                border="black",
            )


def displayTopBarP2(app):
    drawMovementTractor(app, app.p2, app.width - 25 - app.topBarHeight * 4 / 5)
    drawLabel(
        "P2 Score: " + str(app.p2.score), app.width - 150, app.topBarHeight / 2, size=16
    )
    drawRect(
        app.width - 225,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        align="center",
        borderWidth=1,
        fill=None,
        border="black",
    )
    drawRect(
        app.width - 275,
        app.topBarHeight / 2,
        200,
        app.topBarHeight / 2,
        align="right",
        borderWidth=1,
        fill=None,
        border="black",
    )
    if app.p2.powerUp != None:
        drawImage(
            app.imageDict[app.p2.powerUpName],
            app.width - 225,
            app.topBarHeight / 2,
            align="center",
            width=app.topBarHeight / 2,
            height=app.topBarHeight / 2,
        )
        if app.p2.powerUpCoolDown != app.powerUpCoolDown:
            drawRect(
                app.width - 275,
                app.topBarHeight / 2,
                200 * (1 - app.p2.powerUpCoolDown / app.powerUpCoolDown),
                app.topBarHeight / 2,
                borderWidth=1,
                align="right",
                fill="cyan",
                border="black",
            )


def drawMovementTractor(app, player, startX):
    size = app.topBarHeight * 4 / 5
    # draw the board
    drawRect(
        startX,
        app.topBarHeight / 2,
        size,
        size,
        align="left",
        border="black",
        fill=None,
    )
    drawLine(
        startX,
        app.topBarHeight / 2 + size / 6,
        startX + size,
        app.topBarHeight / 2 + size / 6,
    )
    drawLine(
        startX,
        app.topBarHeight / 2 - size / 6,
        startX + size,
        app.topBarHeight / 2 - size / 6,
    )
    drawLine(
        startX + size * 2 / 3,
        app.topBarHeight / 2 - size / 2,
        startX + size * 2 / 3,
        app.topBarHeight / 2 + size / 2,
    )
    drawLine(
        startX + size / 3,
        app.topBarHeight / 2 - size / 2,
        startX + size / 3,
        app.topBarHeight / 2 + size / 2,
    )
    # using AR result
    if not (player.ARVals[0] == 0 and player.ARVals[1] == 0):
        xVal = player.ARVals[0] / (3 / 7) * size + startX
        yVall = player.ARVals[1] * size + app.topBarHeight / 2 - size / 2
        drawCircle(xVal, yVall, 10, fill=player.color)
    # using movement array
    else:
        indices = getIndicesFromMoveDirections(player.moveDirections)
        xVal = indices[0] / 3 * size + startX + size / 6
        yVall = indices[1] / 3 * size + app.topBarHeight / 2 - size / 2 + size / 6
        drawCircle(xVal, yVall, 10, fill=player.color)


def getIndicesFromMoveDirections(movement):
    # for drawing on the board so pretty arbitrary
    ans = [1, 1]
    if movement[0] and not movement[2]:
        ans[1] = 0
    elif movement[2] and not movement[0]:
        ans[1] = 2

    if movement[1] and not movement[3]:
        ans[0] = 0
    elif movement[3] and not movement[1]:
        ans[0] = 2

    return ans
