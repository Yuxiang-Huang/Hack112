def collisionBetweenTwoRects(pos1, w1, h1, pos2, w2, h2):
    return abs(pos1[0] - pos2[0]) < w1 + w2 and abs(pos1[1] - pos2[1]) < h1 + h2


def collisionBetweenTwoCircles(pos1, r1, pos2, r2):
    return dist(pos1[0], pos1[1], pos2[0], pos2[1]) < r1 + r2


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
