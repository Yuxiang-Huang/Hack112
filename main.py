from playerLogic import *
from ui import *
from gameManager import *
from map import *
from imageManager import *
from powerUpManager import *
from startScreen import *

from cmu_graphics import *

import cv2
import mediapipe as mp


def onAppStart(app):
    loadImages(app)
    setDimensions(app)
    createObstacles(app)
    setIntroScreenVaribles(app)


def redrawAll(app):
    if not app.gameStarted:
        drawIntroScreens(app)
    else:
        drawScreen(app)
        displayTopBarP1(app)
        displayTopBarP2(app)
        app.flag1.display()
        app.flag2.display()
        app.p1.display(app)
        app.p2.display(app)
        for rock in app.rocks:
            rock.display()
        for seaweed in app.seaweeds:
            seaweed.display()
        for powerup in app.powerUps:
            powerup.display(app)


def onKeyHold(app, key):
    app.p1.updateDirection(key, True)
    app.p2.updateDirection(key, True)
    app.p1.tryUsePowerUp(app, key)
    app.p2.tryUsePowerUp(app, key)


def onKeyRelease(app, key):
    app.p1.updateDirection(key, False)
    app.p2.updateDirection(key, False)


def onStep(app):
    if app.gameStarted and not app.paused:
        takeStep(app)

    if not app.ARMode:
        return

    # most of the weird stuff here is normal opencv jargon.. etc
    ret, frame = app.cap.read()

    # fliping image
    frame = cv2.flip(frame, 1)

    # change dimension
    frame = cv2.resize(frame, (400, 200))

    # BGR to RGB since mediapipe only works with rgb
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # set flag
    image.flags.writeable = False

    # detections
    results = app.hands.process(image)

    # setting flag to true
    image.flags.writeable = True

    # RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # frame dimensions
    height, width, _ = frame.shape

    # getting fractions to use for line dimensions
    x_seventh = width // 7
    y_thirds = height // 3

    # vertical lines for player 1
    line1 = ((x_seventh, 0), (x_seventh, height))
    line2 = ((x_seventh * 2, 0), (x_seventh * 2, height))
    line3 = ((x_seventh * 3, 0), (x_seventh * 3, height))

    # vertical lines for player 2
    line4 = ((x_seventh * 4, 0), (x_seventh * 4, height))
    line5 = ((x_seventh * 5, 0), (x_seventh * 5, height))
    line6 = ((x_seventh * 6, 0), (x_seventh * 6, height))

    # horizontal lines
    line7 = ((0, y_thirds), (x_seventh * 3, y_thirds))
    line8 = ((0, y_thirds * 2), (x_seventh * 3, y_thirds * 2))
    line9 = ((x_seventh * 4, y_thirds), (width, y_thirds))
    line10 = ((x_seventh * 4, y_thirds * 2), (width, y_thirds * 2))

    # vertical lines
    cv2.line(frame, line1[0], line1[1], (0, 255, 0), 2)
    cv2.line(frame, line2[0], line2[1], (0, 255, 0), 2)
    cv2.line(frame, line3[0], line3[1], (0, 255, 0), 2)

    cv2.line(frame, line4[0], line4[1], (0, 255, 0), 2)
    cv2.line(frame, line5[0], line5[1], (0, 255, 0), 2)
    cv2.line(frame, line6[0], line6[1], (0, 255, 0), 2)

    # horizontal lines
    cv2.line(frame, line7[0], line7[1], (0, 255, 0), 2)
    cv2.line(frame, line8[0], line8[1], (0, 255, 0), 2)
    cv2.line(frame, line9[0], line9[1], (0, 255, 0), 2)
    cv2.line(frame, line10[0], line10[1], (0, 255, 0), 2)

    # overlaying skeleton and checking for fingers up
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            app.mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                app.mp_hands.HAND_CONNECTIONS,
                app.mp_drawing.DrawingSpec(
                    color=(121, 22, 76), thickness=2, circle_radius=4
                ),
                app.mp_drawing.DrawingSpec(
                    color=(250, 44, 250), thickness=2, circle_radius=2
                ),
            )

            # calculating write x coordinate(landmark 0)
            # results.multi_hand_landmarks is a weird non-comma separated list
            # that i spent a while figuring out and reading about to get the
            # wrist landmark for below. the x coord is also given
            # in a value 0-1, so i had to times it by the width
            wrist_x = int(hand_landmarks.landmark[0].x * width)

            # counting the # of extended fingers, needs 4 for powerup
            # ranges from 8,12,16,20 because those re the tips of the finger
            finger_states = [
                int(hand_landmarks.landmark[i].y < hand_landmarks.landmark[i - 2].y)
                for i in range(8, 21, 4)
            ]

            if wrist_x < width / 2:  # left half-player 1
                if sum(finger_states) == 4:
                    # print("Power-Up-Player1")
                    app.p1.tryUsePowerUpARMode(app)
            else:  # right half-player 2
                if sum(finger_states) == 4:
                    # print("Power-Up-Player2")
                    app.p2.tryUsePowerUpARMode(app)

    # getting average
    totalP1X = 0
    totalP1Y = 0

    totalP2X = 0
    totalP2Y = 0

    P1count = 0
    P2count = 0

    if results.multi_hand_landmarks:
        # print(results.multi_hand_landmarks)
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            for landmark in hand_landmarks.landmark:
                if landmark.x <= 3 / 7:
                    totalP1X += landmark.x
                    totalP1Y += landmark.y
                    P1count += 1
                elif landmark.x >= 4 / 7:
                    totalP2X += landmark.x
                    totalP2Y += landmark.y
                    P2count += 1

    if P1count != 0:
        x = totalP1X / P1count
        y = totalP1Y / P1count

        # store value to show on canvas
        app.p1.ARVals[0] = x
        app.p1.ARVals[1] = y

        # player moveDirections = [False, False, False, False] refer to W A S D
        if 0 <= x <= 1 / 7 and 0 <= y <= 1 / 3:
            # print("Up-Left-Player1")
            app.p1.moveDirections = [True, True, False, False]
        elif 1 / 7 <= x <= 2 / 7 and 0 <= y <= 1 / 3:
            # print("Up-Player1")
            app.p1.moveDirections = [True, False, False, False]
        elif 2 / 7 <= x <= 3 / 7 and 0 <= y <= 1 / 3:
            # print("Up-Right-Player1")
            app.p1.moveDirections = [True, False, False, True]

        elif 0 <= x <= 1 / 7 and 1 / 3 <= y <= 2 / 3:
            # print("Left-Player1")
            app.p1.moveDirections = [False, True, False, False]
        elif 1 / 7 <= x <= 2 / 7 and 1 / 3 <= y <= 2 / 3:
            # print("Center-Player1")
            app.p1.moveDirections = [False, False, False, False]
        elif 2 / 7 <= x <= 3 / 7 and 1 / 3 <= y <= 2 / 3:
            # print("Right-Player1")
            app.p1.moveDirections = [False, False, False, True]

        elif 0 <= x <= 1 / 7 and 2 / 3 <= y <= 1:
            # print("Down-Left-Player1")
            app.p1.moveDirections = [False, True, True, False]
        elif 1 / 7 <= x <= 2 / 7 and 2 / 3 <= y <= 1:
            # print("Down-Player1")
            app.p1.moveDirections = [False, False, True, False]
        elif 2 / 7 <= x <= 3 / 7 and 2 / 3 <= y <= 1:
            # print("Down-Right-Player1")
            app.p1.moveDirections = [False, False, True, True]

    if P2count != 0:
        x = totalP2X / P2count
        y = totalP2Y / P2count
        app.p2.ARVals[0] = x
        app.p2.ARVals[1] = y

        if 4 / 7 <= x <= 5 / 7 and 0 <= y <= 1 / 3:
            # print("Up-Left-Player2")
            app.p2.moveDirections = [True, True, False, False]
        elif 5 / 7 <= x <= 6 / 7 and 0 <= y <= 1 / 3:
            # print("Up-Player2")
            app.p2.moveDirections = [False, True, False, False]
        elif 6 / 7 <= x <= 1 and 0 <= y <= 1 / 3:
            # print("Up-Right-Player2")
            app.p2.moveDirections = [True, False, False, True]

        elif 4 / 7 <= x <= 5 / 7 and 1 / 3 <= y <= 2 / 3:
            # print("Left-Player2")
            app.p2.moveDirections = [False, True, False, False]
        elif 5 / 7 <= x <= 6 / 7 and 1 / 3 <= y <= 2 / 3:
            # print("Center-Player2")
            app.p2.moveDirections = [False, False, False, False]
        elif 6 / 7 <= x <= 1 and 1 / 3 <= y <= 2 / 3:
            # print("Right-Player2")
            app.p2.moveDirections = [False, False, False, True]

        elif 4 / 7 <= x <= 5 / 7 and 2 / 3 <= y <= 1:
            # print("Down-Left-Player2")
            app.p2.moveDirections = [False, True, True, False]
        elif 5 / 7 <= x <= 6 / 7 and 2 / 3 <= y <= 1:
            # print("Down-Player2")
            app.p2.moveDirections = [False, False, True, False]
        elif 6 / 7 <= x <= 1 and 2 / 3 <= y <= 1:
            # print("Down-Right-Player2")
            app.p2.moveDirections = [False, False, True, True]

    cv2.imshow("Hand Tracking", frame)


def takeStep(app):
    updateSpawnPowerUp(app)
    app.p1.update(app)
    app.p2.update(app)
    checkPlayerCollision(app)
    checkPlayerFlagCollision(app)
    checkPlayerWin(app)


def main():
    runApp(1400, 700)


main()
