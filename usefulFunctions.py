def collisionBetweenTwoRects(pos1, w1, h1, pos2, w2, h2):
    return (
        abs(pos1[0] - pos2[0]) < w1 / 2 + w2 / 2
        and abs(pos1[1] - pos2[1]) < h1 / 2 + h2 / 2
    )


def collisionBetweenTwoCircles(pos1, r1, pos2, r2):
    return distance(pos1[0], pos1[1], pos2[0], pos2[1]) < r1 + r2


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# normalized direction of pos 1 pushing outnpos 2
def pushOutDir(pos1, pos2):
    # find normalized vector
    vector = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
    return normalize(vector)


def normalize(vector):
    mag = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    vector = [vector[0] / mag, vector[1] / mag]
    return vector
