from cmu_graphics import *


def setDimensions(app):
    app.margin = 50

    app.cameraBoxWidth = 400
    app.cameraBoxHeight = 200

    app.fieldCanvas = {
        "topLeftX": 0,
        "topLeftY": app.cameraBoxHeight,
        "width": app.width,
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
    drawRect(
        app.fieldCanvas["topLeftX"],
        app.fieldCanvas["topLeftY"],
        app.fieldCanvas["width"],
        app.fieldCanvas["height"],
        fill="lightGreen",
    )

    # vertical center line
    drawLine(app.width / 2, 0, app.width / 2, app.height, fill="black")
