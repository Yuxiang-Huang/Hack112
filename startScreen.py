from cmu_graphics import *
def onAppStart(app):
    app.mouseX=0
    app.mouseY=0
    app.used=False
    app.pressedInst=False
    app.pressedStart=False
def onMousePress(app,mouseX,mouseY):
    if  (mouseX<=((app.width*2/3)+200)
    and mouseX>=((app.width*2/3)-200)
    and mouseY<=(app.height*3/4)+50
    and mouseY>=(app.height*3/4)-50):
        app.used=True
        app.pressedInst=True

def startScreen(app):
    drawRect(0,0,app.width,app.height,fill='lightgreen')
    drawLabel('Capture the Flag!!!',app.width/2,app.height/8,size=70,bold=True,fill='red')
    drawRect(app.width/3,(app.height*3/4),300,100,fill='orange',align='center',border='red')
    drawLabel('START!',app.width/3,(app.height*3/4),fill='red',size=70)
    drawRect(app.width*2/3,(app.height*3/4),400,100,fill='grey',align='center',border='white')
    drawLabel('Instructions',app.width*2/3,(app.height*3/4),fill='white',size=70)
    
def instructionsScreen(app):
    drawRect(0,0,app.width,app.height,fill='black')
    drawLabel('How to play',app.width/2,app.height/8,fill='white')



def redrawAll(app):
    if not app.used:
        startScreen(app)
    else:
        instructionsScreen(app)
def main():
    runApp(1200,700)

main()
