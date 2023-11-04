def checkPlayerCollision(app):
    if abs(app.p1.pos[0] - app.p2.pos[0]) < app.p1.size / 2 + app.p2.size / 2:
        if abs(app.p1.pos[1] - app.p2.pos[1]) < app.p1.size / 2 + app.p2.size / 2:
            if app.p1.pos[0] > app.width / 2:
                app.p1.respawn()
            if app.p2.pos[0] < app.width / 2:
                app.p2.respawn()
