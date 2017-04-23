import math

delta = 0.01


def dist(x0, y0, x1, y1):
    return math.hypot(x0 - x1, y0 - y1)


def almost_equal(x, y, z):
    return abs(x - y) < 0.1 and abs(x - z) < 0.1 and abs(y - z) < 0.1


def test(x1, y1, x2, y2, x, y, dist1, dist2):
    new_dist1 = dist(x1, y1, x, y)
    new_dist2 = dist(x2, y2, x, y)
    return abs(new_dist1 - new_dist2) < abs(dist1 - dist2)


def get_new_x_y(x0, y0, x1, y1, x2, y2, x, y):
    dist1 = dist(x1, y1, x, y)
    dist2 = dist(x2, y2, x, y)
    dx = delta if x < x0 else -delta
    dy = delta if y < y0 else -delta
    if test(x1, y1, x2, y2, x + dx, y, dist1, dist2):
        x += dx
    else:
        y += dy
    return x, y


def search(x0, y0, x1, y1, x2, y2):
    x = x0
    y = y0

    while True:

        dist0 = dist(x0, y0, x, y)
        dist1 = dist(x1, y1, x, y)
        dist2 = dist(x2, y2, x, y)

        print "objection function: ", abs(dist0 - dist1) + abs(dist0 - dist2) + abs(dist1 - dist2)
        if almost_equal(dist0, dist1, dist2):
            return x, y

        max_dist = max(dist0, dist1, dist2)
        if max_dist == dist0:
            x, y = get_new_x_y(x0, y0, x1, y1, x2, y2, x, y)
        if max_dist == dist1:
            x, y = get_new_x_y(x1, y1, x0, y0, x2, y2, x, y)
        if max_dist == dist2:
            x, y = get_new_x_y(x2, y2, x1, y1, x0, y0, x, y)


print search(0, 0, 0, 10, 10, 0)


