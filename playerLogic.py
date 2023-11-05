from cmu_graphics import *
from usefulFunctions import *


class Player:
    def __init__(self, moveKeys, powerUpKey, color, spawnPosition):
        self.pos = [spawnPosition[0], spawnPosition[1]]
        self.color = color
        self.hasFlag = False
        self.spawnPosition = spawnPosition
        self.size = 75
        self.speed = 10

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
            # if self == app.p1:
            #     self.drawImageHelper("freeze")
            # else:
            #     self.drawImageHelper("freeze")
        else:
            if self == app.p1:
                if self.frozen:
                    self.drawImageHelper("freeze")
                else:
                    self.drawImageHelper("blueFish")
            else:
                if self.frozen:
                    self.drawImageHelper("freeze")
                else:
                    self.drawImageHelper("redFish")

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

        # decrease freeze time until unfroezen
        if self.frozen:
            self.freezeTime -= 1
            if self.freezeTime < 0:
                self.frozen = False
            return

        # decrease speed if in seaweed
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

        # check collision to get power up
        index = len(app.powerUps) - 1
        while index >= 0:
            if app.powerUps[index].checkCollision(self, app):
                self.powerUp = app.powerUps[index]
                self.powerUpName = app.powerUps[index].name
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

    def tryUsePowerUp(self, app, keys):
        if (
            self.powerUpKey in keys
            and self.powerUpCoolDown <= 0
            and self.powerUp != None
        ):
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


def displayTopBarP1(app):
    drawLabel("P1 Score: " + str(app.p1Score), 50, app.topBarHeight / 2, size=16)
    drawRect(
        125,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        align="center",
        borderWidth=1,
        fill=None,
        border="black",
    )
    drawRect(
        175,
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
            125,
            app.topBarHeight / 2,
            align="center",
            width=app.topBarHeight / 2,
            height=app.topBarHeight / 2,
        )
        if app.p1.powerUpCoolDown != app.powerUpCoolDown:
            drawRect(
                175,
                app.topBarHeight / 2,
                200 * (1 - app.p1.powerUpCoolDown / app.powerUpCoolDown),
                app.topBarHeight / 2,
                borderWidth=1,
                align="left",
                fill="cyan",
                border="black",
            )


def displayTopBarP2(app):
    drawLabel(
        "P2 Score: " + str(app.p2Score), app.width - 50, app.topBarHeight / 2, size=16
    )
    drawRect(
        app.width - 125,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        app.topBarHeight / 2,
        align="center",
        borderWidth=1,
        fill=None,
        border="black",
    )
    drawRect(
        app.width - 175,
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
            app.width - 125,
            app.topBarHeight / 2,
            align="center",
            width=app.topBarHeight / 2,
            height=app.topBarHeight / 2,
        )
        if app.p2.powerUpCoolDown != app.powerUpCoolDown:
            drawRect(
                app.width - 175,
                app.topBarHeight / 2,
                200 * (1 - app.p2.powerUpCoolDown / app.powerUpCoolDown),
                app.topBarHeight / 2,
                borderWidth=1,
                align="right",
                fill="cyan",
                border="black",
            )
