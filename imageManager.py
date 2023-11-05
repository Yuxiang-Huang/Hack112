from cmu_graphics import *
from PIL import Image


def loadImages(app):
    app.width = 1200
    app.height = 700
    # Load the PIL image
    app.imageDict = {
        "freeze": "img/freeze.png",
        "bounceObject": "img/bounceObject.png",
        "mine": "img/mine.png",
        "pushAway": "img/pushAway.png",
        "teleport": "img/teleport.png",
        "rock": "img/rock.png",
        "seaweed": "img/seaweed.png",
    }

    for imgName in app.imageDict:
        fileName = app.imageDict[imgName]
        app.imageDict[imgName] = CMUImage(Image.open(fileName))
