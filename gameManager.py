def checkPlayerCollision(app):
    if abs(app.p1.pos[0] - app.p2.pos[0]) < app.p1.size / 2 + app.p2.size / 2:
        if abs(app.p1.pos[1] - app.p2.pos[1]) < app.p1.size / 2 + app.p2.size / 2:
            if app.p1.pos[0] > app.width / 2:
                app.p1.respawn(app.flag2)
            if app.p2.pos[0] < app.width / 2:
                app.p2.respawn(app.flag1)


def checkPlayerFlagCollision(app):
    if app.flag1.checkCollision(app.p2):
        app.p2.hasFlag = True
        app.flag1.captured = True
    if app.flag2.checkCollision(app.p1):
        app.p1.hasFlag = True
        app.flag2.captured = True


def checkPlayerWin(app):
    if app.p1.hasFlag and app.p1.pos[0] < app.margin:
        app.p1score += 1
        app.p1.hasFlag = False
        app.flag2.captured = False
    if app.p2.hasFlag and app.p2.pos[0] > app.width - app.margin:
        app.p2score += 1
        app.p2.hasFlag = False
        app.flag1.captured = False
