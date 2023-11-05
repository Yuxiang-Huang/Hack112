from cmu_graphics import *
from imageManager import *


def setDimensions(app):
    app.margin = 50
    app.topBarHeight = 75

    app.fieldCanvas = {
        "topLeftY": app.topBarHeight,
        "height": app.height - app.topBarHeight,
    }


def drawScreen(app):
    # time text for power up
    if len(app.powerUps) == 0:
        drawLabel(
            f"{app.timeUntilSpawn // 60 + 1} seconds until next power up spawn",
            app.width / 2,
            app.topBarHeight / 2,
            size=20,
        )
        # align="center"

    # field
    drawImage(
        app.imageDict["oceanBackground"],
        0,
        390,
        width=app.width * 2,
        height=app.fieldCanvas["height"],
        align="center",
    )

    # score
    drawLabel(f"current points: x", 100, app.topBarHeight / 2, size=16)
    drawLabel(f"current points: y", app.width - 100, app.topBarHeight / 2, size=16)

    # vertical center line
    drawLine(app.width / 2, 0, app.width / 2, app.height, fill="black")


def oceanTheme():
    colorPalette = {"oceanBlue": rgb(95, 123, 165), "rock": rgb(73, 70, 67)}
    procreateBrush = {"rock": "Syrup"}
