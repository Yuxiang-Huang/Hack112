from cmu_graphics import *
from playerLogic import *
from ui import *
from gameManager import *
from map import *


def onAppStart(app):
    setDimensions(app)
    createObstacles(app)

    # create player and flag objects
    middleYVal = app.fieldCanvas["topLeftY"] + app.fieldCanvas["height"] / 2
    app.p1 = Player(["w", "a", "s", "d"], "blue", (app.margin * 2 / 3, middleYVal))
    app.p2 = Player(
        ["up", "left", "down", "right"],
        "red",
        (app.width - app.margin * 2 / 3, middleYVal),
    )
    app.flag1 = Flag(app, (app.margin * 2, middleYVal))
    app.flag2 = Flag(app, (app.width - app.margin * 2, middleYVal))

    app.paused = False


def redrawAll(app):
    drawScreen(app)
    app.flag1.display()
    app.flag2.display()
    app.p1.display()
    app.p2.display()
    for rock in app.rocks:
        rock.display()
    for seaweed in app.seaweeds:
        seaweed.display()


def onKeyHold(app, key):
    app.p1.updateDirection(key, True)
    app.p2.updateDirection(key, True)


def onKeyRelease(app, key):
    app.p1.updateDirection(key, False)
    app.p2.updateDirection(key, False)


def onStep(app):
    if not app.paused:
        takeStep(app)


def takeStep(app):
    app.p1.update(app)
    app.p2.update(app)
    checkPlayerCollision(app)


def main():
    runApp(1200, 700)


main()
