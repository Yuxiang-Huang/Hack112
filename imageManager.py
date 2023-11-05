from cmu_graphics import *
from PIL import Image


def loadImages(app):
    # Load the PIL image
    app.imageDict = {
        "freeze": "img/freeze.png",
        "bounceObject": "img/bounceObject.png",
        "mine": "img/mine.png",
        "pushAway": "img/pushAway.png",
        "teleport": "img/teleport.png",
        "rock": "img/rock.png",
        "seaweed": "img/seaweed.png",
        "oyster-pearl": "img/oysterWithPearl.png",
        "oyster": "img/closedOyster.png",
        "oceanBackground": "img/oceanBackground.png",
        "goldFish": "img/goldFishGoingLeft.png",
        "blueFish": "img/blueGoldFishGoingRight.png",
        "redFish": "img/redGoldFishGoingLeft.png",
        "clock": "img/clock.png",
        "frozenRedFish": "img/frozenRedFish.png",
        "frozenBlueFish": "img/frozenBlueFish.png"
    }

    for imgName in app.imageDict:
        fileName = app.imageDict[imgName]
        app.imageDict[imgName] = CMUImage(Image.open(fileName))
