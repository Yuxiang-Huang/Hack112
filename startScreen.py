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
            mouseX <= (1100)
            and mouseX >= (300)
            and mouseY <= (app.height * 2 / 5) + 50
            and mouseY >= (app.height * 2 / 5) - 50
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
            mouseX <= app.width / 2 + 75
            and mouseX >= app.width / 2 - 75
            and mouseY <= app.height * 11 / 12 + 35
            and mouseY >= app.height * 11 / 12 - 35
        ):
            app.screenIndex += 1
            # out of bound to return to home screen
            if app.screenIndex == len(app.screens):
                app.screenIndex = 0
                app.infoScreen = False


def startScreen(app):
    # the background color
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    # the title
    drawLabel(
        "Capture the Flag!!!",
        app.width / 2,
        app.height / 8,
        size=70,
        bold=True,
        fill="white",
    )
    
    # start with AR
    drawRect(
        app.width / 2,
        (app.height *2 / 5),
        500,
        100,
        fill=rgb(129, 114, 177),
        align="center",
        border="white",
    )
    drawLabel("START with AR", app.width / 2, (app.height * 2/ 5), fill="blue", size=40)
    
    # start with keyboard
    drawRect(
        app.width / 2,
        (app.height *3 / 5),
        500,
        100,
        fill=rgb(129, 114, 177),
        align="center",
        border="white",
    )
    drawLabel("START with keyboard", app.width / 2, (app.height * 3/ 5), fill="red", size=40)

    # instructions
    drawRect(
        app.width / 2,
        (app.height *4 / 5),
        500,
        100,
        fill="gray",
        align="center",
        border="white",
    )
    drawLabel("Instructions", app.width / 2, (app.height * 4/ 5), fill="white", size=40)

def drawNextButton(app):
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


def drawSimpleFishToPearl(app):
    drawImage(
        app.imageDict["blueFish"],
        200,
        app.height / 2,
        align="center",
        width=75,
        height=75,
    )
    drawLine(
        275,
        app.height / 2,
        app.width - 275,
        app.height / 2,
        arrowEnd=True,
        fill="white",
    )
    drawImage(
        app.imageDict["oyster-pearl"],
        app.width - 200,
        app.height / 2,
        align="center",
        width=100,
        height=100,
    )


def instructionsScreen1(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawLabel(
        "Capture their flag!!!", app.width / 2, app.height / 4, fill="white", size=50
    )
    drawSimpleFishToPearl(app)
    drawNextButton(app)


def instructionsScreen2(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
    drawLabel(
        "Return the flag!!!", app.width / 2, app.height / 4, fill="white", size=50
    )
    drawLine(
        275,
        app.height / 2,
        app.width - 275,
        app.height / 2,
        arrowStart=True,
        fill="white",
    )
    drawImage(
        app.imageDict["redFishPearl"],
        200,
        app.height / 2,
        align="center",
        width=75,
        height=75,
    )
    drawImage(
        app.imageDict["oyster"],
        app.width - 200,
        app.height / 2,
        align="center",
        width=100,
        height=100,
    )
    drawNextButton(app)


def instructionsScreen3(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("How to play", app.width / 2, app.height / 8, fill="white", size=80)
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
    drawSimpleFishToPearl(app)
    drawNextButton(app)

    drawImage(
        app.imageDict["seaweed"],
        app.width / 2 - 100,
        app.height / 2,
        align="center",
        width=50,
        height=100,
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
    drawImage(
        app.imageDict["oyster-pearl"],
        app.width - 100,
        app.height / 2,
        align="center",
        width=100,
        height=100,
    )

    drawImage(
        app.imageDict["blueFish"],
        100,
        app.height / 2,
        align="center",
        width=75,
        height=75,
    )

    drawImage(
        app.imageDict["blueFish"],
        100,
        app.height / 2 - 60,
        align="center",
        width=75,
        height=75,
        opacity=25,
    )

    drawNextButton(app)

    drawImage(
        app.imageDict["blueFish"],
        app.width / 2 + 50,
        app.height / 2 - 60,
        align="center",
        width=75,
        height=75,
    )

    drawImage(
        app.imageDict["redFish"],
        app.width / 2 + 120,
        app.height / 2 - 60,
        align="center",
        width=75,
        height=75,
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
    drawLabel("Power-Ups", app.width / 2, app.height / 8, fill="white", size=80)
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
        "Teleport forward",
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
        "Push the enemy away",
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
    drawNextButton(app)


def instructionsScreen6(app):
    drawRect(0, 0, app.width, app.height, fill=rgb(109, 149, 197))
    drawLabel("Power-Ups", app.width / 2, app.height / 8, fill="white", size=80)
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
        "Drop a mine to trap the enemy",
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
