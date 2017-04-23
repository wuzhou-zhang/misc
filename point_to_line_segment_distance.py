import math


def dist(x0, y0, x1, y1):
    return math.hypot(x0 - x1, y0 - y1)


def binary_search(x0, y0, x1, y1, x, y):
    while dist(x0, y0, x1, y1) > 0.01:
        dist0 = dist(x0, y0, x, y)
        dist1 = dist(x1, y1, x, y)
        middle_x = (x0 + x1) / 2.0
        middle_y = (y0 + y1) / 2.0
        new_dist = dist(middle_x, middle_y, x, y)
        if dist0 < new_dist < dist1:
            return dist0, x0, y0
        if dist1 < new_dist < dist0:
            return dist1, x1, y1
        if dist1 > dist0:
            x1 = middle_x
            y1 = middle_y
        else:
            x0 = middle_x
            y0 = middle_y

    middle_x = (x0 + x1) / 2.0
    middle_y = (y0 + y1) / 2.0
    return dist(middle_x, middle_y, x, y), middle_x, middle_y

print binary_search(0, 1, 1, 4, 3, 3)
