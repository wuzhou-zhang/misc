import math


def get_convergence(x0, y0, x1, y1, x2, y2, x, y):
    dist0 = math.hypot(x0 - x, y0 - y)
    dist1 = math.hypot(x1 - x, y1 - y)
    dist2 = math.hypot(x2 - x, y2 - y)
    return abs(dist0 - dist1) + abs(dist0 - dist2) + abs(dist1 - dist2)


def iterative_search(x0, y0, x1, y1, x2, y2):
    x, y, convergence, delta = x0, y0, 1e9, 0.05
    while convergence > 0.1:
        convergence = get_convergence(x0, y0, x1, y1, x2, y2, x, y)
        for (new_x, new_y) in (x + delta, y), (x - delta, y), (x, y + delta), (x, y - delta):
            if get_convergence(x0, y0, x1, y1, x2, y2, new_x, new_y) < convergence:
                x, y = new_x, new_y
    return x, y

print iterative_search(0, 0, 0, 10, 10, 0)
