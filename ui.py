from cmu_graphics import *


def setDimensions(app):
    app.margin = 50
    app.topBarHeight = 75

    app.fieldCanvas = {
        "topLeftY": app.topBarHeight,
        "height": app.height - app.topBarHeight,
    }


def drawScreen(app):
    # field
    drawRect(
        0,
        app.fieldCanvas["topLeftY"],
        app.width,
        app.fieldCanvas["height"],
        fill="lightGreen",
    )

    # score
    # drawLabel()

    # vertical center line
    drawLine(app.width / 2, 0, app.width / 2, app.height, fill="black")


def oceanTheme():
    colorPalette = {"oceanBlue": rgb(95, 123, 165), "rock": rgb(73, 70, 67)}
    procreateBrush = {"rock": "Syrup"}
