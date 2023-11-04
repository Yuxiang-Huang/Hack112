from cmu_graphics import *
from playerLogic import *
from ui import *


def onAppStart(app):
    setDimensions(app)

    app.p1 = Player(["w", "a", "s", "d"], "blue")
    app.p2 = Player(["up", "left", "down", "right"], "red")
    app.paused = False


def redrawAll(app):
    drawScreen(app)
    app.p1.drawCharacter()
    app.p2.drawCharacter()


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
    app.p1.update()
    app.p2.update()


def main():
    runApp(1200, 700)


main()
