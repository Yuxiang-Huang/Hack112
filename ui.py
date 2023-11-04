from cmu_graphics import *

# import cv2


def setDimensions(app):
    app.cameraBoxWidth = 400
    app.cameraBoxHeight = 200
    app.flagImg = readImage("img/flagImg.png")

    app.fieldDimensions = [
        0,
        app.cameraBoxHeight,
        app.width,
        app.height - app.cameraBoxHeight,
    ]  # topLeftX, topLeftY, width, height

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
        app.fieldDimensions[0],
        app.fieldDimensions[1],
        app.fieldDimensions[2],
        app.fieldDimensions[3],
        fill="lightGreen",
    )

    # vertical center line
    drawLine(app.width / 2, 0, app.width / 2, app.height, fill="black")

    # flags
    drawFlags(app)


def drawFlags(app):
    leftFlagY = app.cameraBoxHeight + ((app.fieldDimensions[3] - 100) // 2)
    rightFlagX = app.width - app.flagWidth

    # drawImage(app.flagImg, 0, leftFlagY, align='center',
    #           width=app.flagWidth, height=app.flagHeight)

    drawRect(0, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
    drawRect(rightFlagX, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
