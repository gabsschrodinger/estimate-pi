import random as r

def estimate_pi(n):
    points = [(r.uniform(-1,1), r.uniform(-1,1)) for _ in range(n)]
    points_inside = [(x,y) for (x,y) in points if x**2 + y**2 < 1]
    return 4 * len(points_inside) / len(points)

print("Pi value: " + str(estimate_pi(26666667)))