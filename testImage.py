from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.width = 1200
    app.height = 700
    # Load the PIL image
    app.imageDict = ({"freeze": "img/freeze.png", "bounceObject": "img/bounceObject.png", 
                      "mine": "img/mine.png", "pushAway": "img/pushAway.png", 
                      "teleport": "img/teleport.png", "rock": "img/rock.png", 
                      "seaweed": "img/seaweed.png"})
    
    for imgName in app.imageDict:
        fileName = app.imageDict[imgName]
        app.imageDict[imgName] = CMUImage(Image.open(fileName))
   
    
    # app.image = Image.open("img/rock.png")
    
    # Convert each PIL image to a CMUImage for drawing
    # app.image = CMUImage(app.image)
    
def redrawAll(app):
    
    #scaled image
    drawLabel('Scaled', 500, 50, align='center', size=24)
    
    i = 0
    for imgName in app.imageDict: # i increases the x value
        pilImage = app.imageDict[imgName].image
        drawImage(app.imageDict[imgName], 100 + i, 200, align='center',
              width=100,
              height=100)
        i += 100
    
    seaweedPilImage = app.imageDict['seaweed'].image
    drawImage(app.imageDict["seaweed"], 500, 400, align='center', width = 150, height=200)

def main():
    runApp()

main()