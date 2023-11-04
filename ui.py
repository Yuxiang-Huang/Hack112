from cmu_graphics import *
# import cv2

# imageWidth, imageHeight = getImageSize(app.url)

# drawLabel(f'Original ({imageWidth}x{imageHeight})', 125, 75, size=16)
# drawImage(app.url, 125, 200, align='center')


def setDimensions(app):
    app.cameraBoxWidth = 400
    app.cameraBoxHeight = 200
    # app.flagImg = readImage('img/flagImg.png')
    
    
    app.fieldDimensions = [
        0,
        app.cameraBoxHeight,
        app.width,
        app.height - app.cameraBoxHeight,
    ]  # topLeftX, topLeftY, width, height

    app.flagHeight = 200
    app.flagWidth = 100

# app.url = "https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg"


def readImage(filename):
    with open(filename, encoding='utf-8') as f:
        fileString = f.read()
    return fileString

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

    # flags
    drawFlags(app)


def drawFlags(app):
    leftFlagY = app.cameraBoxHeight + ((app.fieldDimensions[3] - 200) // 2)
    rightFlagX = app.width - app.flagWidth

    # # drawImage(app.flagImg, 0, leftFlagY, align='center',
    #           width=app.flagWidth, height=app.flagHeight)

    drawRect(0, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
    drawRect(rightFlagX, leftFlagY, app.flagWidth, app.flagHeight, fill="red")
