def equilateral(sides):
    return len(set(sides)) == 1 and set(sides) != {0}


def isosceles(sides):
    if sides[0] + sides[1] < sides[2] or sides[2] + sides[1] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    return (len(set(sides)) == 2 or len(set(sides)) == 1) and set(sides) != {0}


def scalene(sides):
    if sides[0] + sides[1] < sides[2] or sides[2] + sides[1] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False
    return len(set(sides)) == 3 and set(sides) != {0}
