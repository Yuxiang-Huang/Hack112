from playerLogic import *
from map import *
import cv2
import mediapipe as mp
from playsound import playsound


def startGame(app, ARMode):
    app.paused = False

    # create player and flag objects
    middleYVal = app.fieldCanvas["topLeftY"] + app.fieldCanvas["height"] / 2
    app.p1 = Player(["w", "a", "s", "d"], "e", "blue", (app.margin * 2 / 3, middleYVal))
    app.p2 = Player(
        ["up", "left", "down", "right"],
        "/",
        "red",
        (app.width - app.margin * 2 / 3, middleYVal),
    )
    app.flag1 = Flag(app, (app.margin * 2, middleYVal))
    app.flag2 = Flag(app, (app.width - app.margin * 2, middleYVal))

    # power ups
    app.powerUps = []
    app.powerUpSpawnTime = 150
    app.timeUntilSpawn = app.powerUpSpawnTime
    app.powerUpSize = 45
    app.powerUpCoolDown = 150

    # AR Mode set up
    if ARMode:
        app.ARMode = True
        app.mp_drawing = mp.solutions.drawing_utils
        app.mp_hands = mp.solutions.hands
        app.cap = cv2.VideoCapture(0)
        app.hands = app.mp_hands.Hands(
            min_detection_confidence=0.8, min_tracking_confidence=0.5
        )


def checkPlayerCollision(app):
    if abs(app.p1.pos[0] - app.p2.pos[0]) < app.p1.size / 2 + app.p2.size / 2:
        if abs(app.p1.pos[1] - app.p2.pos[1]) < app.p1.size / 2 + app.p2.size / 2:
            if app.p1.pos[0] > app.width / 2:
                app.p2.getPowerUp(app.p1)
                app.p1.respawn(app.flag2)
            if app.p2.pos[0] < app.width / 2:
                app.p1.getPowerUp(app.p2)
                app.p2.respawn(app.flag1)


def checkPlayerFlagCollision(app):
    if app.flag1.checkCollision(app.p2):
        app.p2.hasFlag = True
        app.flag1.captured = True
    if app.flag2.checkCollision(app.p1):
        app.p1.hasFlag = True
        app.flag2.captured = True


def checkPlayerWin(app):
    if app.p1.hasFlag and app.p1.pos[0] < app.p1.size:
        app.p1.score += 1
        app.p1.hasFlag = False
        playsound("img/winningSound.wav")
        app.p1.resetPowerUp()
        app.flag2.captured = False

    if app.p2.hasFlag and app.p2.pos[0] > app.width - app.p2.size:
        app.p2.score += 1
        app.p2.resetPowerUp()
        playsound("img/winningSound.wav")
        app.p2.hasFlag = False
        app.flag1.captured = False
