from cmu_graphics import *
from imageManager import *
from gameManager import *


def setIntroScreenVaribles(app):
    app.ARMode = False
    app.screenIndex = 0
    app.infoScreen = False
    app.gameStarted = False
    app.screens = [
        instructionsScreen1,
        instructionsScreen2,
        instructionsScreen3,
        instructionsScreen4,
        instructionsScreen5,
        instructionsScreen6,
    ]


def onMousePress(app, mouseX, mouseY):
    if not app.infoScreen:
        # start game without AR
        if (
            mouseX <= ((app.width / 3) + 150)
            and mouseX >= ((app.width / 3) - 150)
            and mouseY <= (app.height * 3 / 4) + 50
            and mouseY >= (app.height * 3 / 4) - 50
        ):
            startGame(app, False)
            app.gameStarted = True
        #  start game with AR
        elif mouseX <= (100) and mouseX >= (0) and mouseY <= (100) and mouseY >= (0):
            startGame(app, True)
            app.gameStarted = True
        # start slide show
        elif (
            mouseX <= ((app.width * 2 / 3) + 200)
            and mouseX >= ((app.width * 2 / 3) - 200)
            and mouseY <= (app.height * 3 / 4) + 50
            and mouseY >= (app.height * 3 / 4) - 50
        ):
            app.infoScreen = True
    else:
        # slideshow button
        if (
            mouseX <= app.width / 2 + 150
            and mouseX >= app.width / 2 - 150
            and mouseY <= app.height * 3 / 4 + 50
            and mouseY >= app.height * 3 / 4 - 50
        ):
            app.screenIndex += 1
            # out of bound to return to home screen
            if app.screenIndex == len(app.screens):
                app.screenIndex = 0
                app.infoScreen = False


def startScreen(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel(
        "Capture the Flag!!!",
        app.width / 2,
        app.height / 8,
        size=70,
        bold=True,
        fill="white",
    )
    drawRect(
        app.width / 3,
        (app.height * 3 / 4),
        300,
        100,
        fill="lightgreen",
        align="center",
        border="white",
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


def instructionsScreen1(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawImage(
        app.imageDict["redFish"],
        75,
        app.height / 2,
        align="center",
        width=50,
        height=50,
    )

    drawLabel(
        "Capture their flag!!!", app.width / 2, app.height / 4, fill="white", size=50
    )
    drawLine(
        100,
        app.height / 2,
        app.width - 100,
        app.height / 2,
        arrowEnd=True,
        fill="white",
    )
    drawImage(
        app.imageDict["oyster-pearl"],
        app.width - 75,
        app.height / 2,
        align="center",
        width=50,
        height=50,
    )
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
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
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
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
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
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
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
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("Powerups", app.width / 2, app.height / 8, fill="white", size=80)
    drawLabel(
        "open your hand or press either",
        app.width / 2,
        app.height / 4 - 20,
        fill="white",
        size=30,
    )
    drawLabel(
        "E or / depending on whether",
        app.width / 2,
        app.height / 4 + 10,
        fill="white",
        size=30,
    )
    drawLabel(
        "you are using WASD or the arrow",
        app.width / 2,
        app.height / 4 + 40,
        fill="white",
        size=30,
    )
    drawLabel(
        "keys to move your character",
        app.width / 2,
        app.height / 4 + 70,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["teleport"],
        app.width / 2 - 250,
        app.height / 2 - 5,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Teleport in a random direction",
        app.width / 2 + 20,
        app.height / 2 - 5,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["pushAway"],
        app.width / 2 - 250,
        app.height / 2 + 100,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Push enemys within a radius away",
        app.width / 2 + 20,
        app.height / 2 + 105,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["freeze"],
        app.width / 2 - 250,
        app.height / 2 + 205,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Freeze the enemy",
        app.width / 2 + 20,
        app.height / 2 - 5 + 210,
        fill="white",
        size=30,
    )
    drawRect(
        app.width / 2,
        app.height * 11 / 12,
        150,
        70,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 11 / 12, fill="white", size=50)


def instructionsScreen6(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("Powerups", app.width / 2, app.height / 8, fill="white", size=80)
    drawLabel(
        "open your hand or press either",
        app.width / 2,
        app.height / 4 - 20,
        fill="white",
        size=30,
    )
    drawLabel(
        "E or / depending on whether",
        app.width / 2,
        app.height / 4 + 10,
        fill="white",
        size=30,
    )
    drawLabel(
        "you are using WASD or the arrow",
        app.width / 2,
        app.height / 4 + 40,
        fill="white",
        size=30,
    )
    drawLabel(
        "keys to move your character",
        app.width / 2,
        app.height / 4 + 70,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["mine"],
        app.width / 2 - 250,
        app.height / 2 - 5,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Drop a mine to trap enemys",
        app.width / 2 + 20,
        app.height / 2 - 5,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["bootWithWings"],
        app.width / 2 - 250,
        app.height / 2 + 100,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Speed your up",
        app.width / 2 + 20,
        app.height / 2 + 105,
        fill="white",
        size=30,
    )
    drawImage(
        app.imageDict["clock"],
        app.width / 2 - 250,
        app.height / 2 + 205,
        align="center",
        width=75,
        height=75,
    )
    drawLabel(
        "Sets you back in time",
        app.width / 2 + 20,
        app.height / 2 - 5 + 210,
        fill="white",
        size=30,
    )
    drawRect(
        app.width / 2,
        app.height * 11 / 12,
        150,
        70,
        fill="grey",
        align="center",
        border="white",
    )
    drawLabel("Next", app.width / 2, app.height * 11 / 12, fill="white", size=50)


def drawIntroScreens(app):
    if not app.infoScreen:
        startScreen(app)
    else:
        app.screens[app.screenIndex](app)
