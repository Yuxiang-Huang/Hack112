from cmu_graphics import *
from PIL import Image


def loadImages(app):
    # Load the PIL image
    app.imageDict = {
        "freeze": "img/freeze.png",
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
        "frozenBlueFish": "img/frozenBlueFish.png",
        "redFishPearl": "img/redFishWithPearl.png",
        "blueFishPearl": "img/blueFishWithPearl.png",
        "redFishWind": "img/redFishWithWind.png",
        "blueFishWind": "img/blueFishWithWind.png",
        "bootWithWings": "img/bootWithWings.png"
    }

    for imgName in app.imageDict:
        fileName = app.imageDict[imgName]
        app.imageDict[imgName] = CMUImage(Image.open(fileName))
