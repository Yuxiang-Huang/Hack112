from cmu_graphics import *

# import cv2


def setDimensions(app):
    app.cameraBoxWidth = 400
    app.cameraBoxHeight = 200
    app.flagImg = readImage("img/flagImg.png")

    app.fieldCanvas = {
        "topLeftX": 0,
        "topLeftY": app.cameraBoxHeight,
        "width": app.width,
        "height": app.height - app.cameraBoxHeight,
    }

    app.flagHeight = 100
    app.flagWidth = 50


# app.url = "https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg"


def readImage(filename):
    # Save image in set directory
    # Read RGB image
    # img = cv2.imread('filename')
    # return img
    pass


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

    # flags
    drawFlags(app)


def drawFlags(app):
    leftFlagY = app.cameraBoxHeight + ((app.fieldCanvas["width"] - 100) // 2)
    rightFlagX = app.width - app.flagWidth

    # drawImage(app.flagImg, 0, leftFlagY, align='center',
    #           width=app.flagWidth, height=app.flagHeight)

    drawRect(0, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
    drawRect(rightFlagX, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
