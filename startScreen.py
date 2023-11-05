from cmu_graphics import *
from imageManager import *


def setIntroScreenVaribles(app):
    app.mouseX = 0
    app.mouseY = 0
    app.screenIndex = 0
    app.infoScreen = False
    app.pressedStart = False
    app.screens = [
        instructionsScreen1,
        instructionsScreen2,
        instructionsScreen3,
        instructionsScreen4,
        instructionsScreen5,
    ]
    loadImages(app)


def onMousePress(app, mouseX, mouseY):
    if (
        mouseX <= ((app.width / 3) + 150)
        and mouseX >= ((app.width / 3) - 150)
        and mouseY <= (app.height * 3 / 4) + 50
        and mouseY >= (app.height * 3 / 4) - 50
    ):
        app.pressedStart = True
    elif (
        not app.infoScreen
        and mouseX <= ((app.width * 2 / 3) + 200)
        and mouseX >= ((app.width * 2 / 3) - 200)
        and mouseY <= (app.height * 3 / 4) + 50
        and mouseY >= (app.height * 3 / 4) - 50
    ):
        app.infoScreen = True
    elif (
        app.infoScreen
        and mouseX <= app.width / 2 + 150
        and mouseX >= app.width / 2 - 150
        and mouseY <= app.height * 3 / 4 + 50
        and mouseY >= app.height * 3 / 4 - 50
    ):
        app.screenIndex += 1
        if app.screenIndex == len(app.screens):
            app.screenIndex = 0
            app.infoScreen = False


def startScreen(app):
    drawRect(0, 0, app.width, app.height, fill="lightgreen")
    drawLabel(
        "Capture the Flag!!!",
        app.width / 2,
        app.height / 8,
        size=70,
        bold=True,
        fill="red",
    )
    drawRect(
        app.width / 3,
        (app.height * 3 / 4),
        300,
        100,
        fill="orange",
        align="center",
        border="red",
    )
    drawLabel("START!", app.width / 3, (app.height * 3 / 4), fill="red", size=70)
    drawRect(
        app.width * 2 / 3,
        (app.height * 3 / 4),
        400,
        100,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel(
        "Instructions", app.width * 2 / 3, (app.height * 3 / 4), fill="white", size=70
    )
    drawImage(app.imageDict["oyster"], 100, 100, align="center", width=100, height=100)


def instructionsScreen1(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawRect(75, app.height / 2, 50, 50, fill="red", align="center")
    drawLabel(
        "Capture their flag!!!", app.width / 2, app.height / 4, fill="white", size=50
    )
    drawLine(100, app.height / 2, 1100, app.height / 2, arrowEnd=True, fill="white")
    drawRect(1105, app.height / 2, 10, 50, fill="grey", align="center")
    drawRect(1110, app.height / 2 - 25, 40, 20, fill="red", align="bottom-right")
    drawRect(
        app.width / 2,
        app.height * 3 / 4,
        300,
        100,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 3 / 4, fill="white", size=70)


def instructionsScreen2(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawRect(1100, app.height / 2, 50, 50, fill="purple", align="left")
    drawLabel(
        "Return the flag!!!", app.width / 2, app.height / 4, fill="white", size=50
    )
    drawLine(100, app.height / 2, 1100, app.height / 2, arrowStart=True, fill="white")
    drawRect(1105, app.height / 2, 10, 50, fill="grey", align="center")
    drawRect(1110, app.height / 2 - 25, 40, 20, fill="red", align="bottom-right")
    drawRect(75, app.height / 2, 50, 50, fill="red", align="center", opacity=50)
    drawRect(
        app.width / 2,
        app.height * 3 / 4,
        300,
        100,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 3 / 4, fill="white", size=70)


def instructionsScreen3(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawRect(1150, app.height / 2, 40, 50, fill="red", align="right", opacity=40)
    drawLabel(
        "Watch out for rocks and seaweed",
        app.width / 2,
        app.height / 4 - 20,
        fill="white",
        size=40,
    )
    drawLabel(
        "seaweed slows you down and",
        app.width / 2,
        app.height / 4 + 15,
        fill="white",
        size=40,
    )
    drawLabel(
        "you cannot pass through rocks",
        app.width / 2,
        app.height / 4 + 50,
        fill="white",
        size=40,
    )
    drawLine(100, app.height / 2, 1100, app.height / 2, arrowEnd=True, fill="white")
    drawRect(1105, app.height / 2, 10, 50, fill="grey", align="center", opacity=40)
    drawRect(
        1110, app.height / 2 - 25, 40, 20, fill="red", align="bottom-right", opacity=40
    )
    drawRect(75, app.height / 2, 50, 50, fill="red", align="center")
    drawRect(
        app.width / 2,
        app.height * 3 / 4,
        300,
        100,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 3 / 4, fill="white", size=70)
    drawRect(
        app.width / 2 - 100,
        app.height / 2,
        50,
        50,
        align="center",
        fill="red",
        opacity=75,
    )
    drawImage(
        app.imageDict["seaweed"],
        app.width / 2 - 100,
        app.height / 2,
        align="center",
        width=100,
        height=100,
    )
    drawRect(
        app.width / 2 + 100,
        app.height / 2 - 60,
        50,
        50,
        align="center",
        fill="red",
        opacity=50,
    )
    drawImage(
        app.imageDict["rock"],
        app.width / 2 + 100,
        app.height / 2,
        align="center",
        width=100,
        height=100,
    )


def instructionsScreen4(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    drawLine(
        app.width / 2, app.height / 4 + 80, app.width / 2, app.height, fill="white"
    )
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawRect(
        1150,
        app.height / 2,
        50,
        50,
        fill="blue",
        align="right",
    )
    drawLabel(
        "If you touch the enemy while",
        app.width / 2,
        app.height / 4 - 20,
        fill="white",
        size=40,
    )
    drawLabel(
        "in their half of the map you",
        app.width / 2,
        app.height / 4 + 15,
        fill="white",
        size=40,
    )
    drawLabel(
        "die and respawn on your side",
        app.width / 2,
        app.height / 4 + 50,
        fill="white",
        size=40,
    )
    drawLine(
        100,
        app.height / 2,
        app.width / 2 + 25,
        app.height / 2 - 60,
        arrowEnd=True,
        fill="white",
    )
    drawRect(1105, app.height / 2, 10, 50, fill="grey", align="center")
    drawRect(1110, app.height / 2 - 25, 40, 20, fill="red", align="bottom-right")
    drawRect(75, app.height / 2, 50, 50, fill="red", align="center")
    drawRect(75, app.height / 2 - 60, 50, 50, fill="red", align="center", opacity=25)
    drawRect(
        app.width / 2,
        app.height * 3 / 4,
        300,
        100,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 3 / 4, fill="white", size=70)
    drawRect(
        app.width / 2 + 50,
        app.height / 2 - 60,
        50,
        50,
        align="center",
        fill="red",
        opacity=50,
    )
    drawRect(
        app.width / 2 + 100,
        app.height / 2 - 60,
        50,
        50,
        align="center",
        fill="blue",
        opacity=50,
    )
    drawLine(
        app.width / 2 + 25,
        app.height / 2 - 60,
        100,
        app.height / 2 - 60,
        arrowEnd=True,
        fill="white",
    )


def instructionsScreen5(app):
    drawRect(0, 0, app.width, app.height, fill="black")
    drawLabel("Powerups", app.width / 2, app.height / 8, fill="white", size=80)
    drawLabel(
        "If you touch the enemy while",
        app.width / 2,
        app.height / 4 - 20,
        fill="white",
        size=40,
    )


def drawIntroScreens(app):
    if not app.infoScreen:
        startScreen(app)
    else:
        app.screens[app.screenIndex](app)
