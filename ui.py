from cmu_graphics import *
from imageManager import *


def setDimensions(app):
    app.margin = 50

    app.cameraBoxWidth = 400
    app.cameraBoxHeight = 200

    app.fieldCanvas = {
        "topLeftY": app.cameraBoxHeight,
        "height": app.height - app.cameraBoxHeight,
    }


def drawScreen(app):
    # camera boxes
    drawRect(0, 0, app.cameraBoxWidth, app.cameraBoxHeight, border="black", fill=None)
    drawRect(
        app.width - app.cameraBoxWidth,
        0,
        app.cameraBoxWidth,
        app.cameraBoxHeight,
        border="black",
        fill=None,
    )

    # field
    drawImage(
        app.imageDict["oceanBackground"],
        0,
        app.fieldCanvas["topLeftY"],
        align="center",
        width=app.width,
        height=app.fieldCanvas["height"],
    )

    # score
    # drawLabel()

    # vertical center line
    drawLine(app.width / 2, 0, app.width / 2, app.height, fill="black")


def oceanTheme():
    colorPalette = {"oceanBlue": rgb(95, 123, 165), "rock": rgb(73, 70, 67)}
    procreateBrush = {"rock": "Syrup"}
