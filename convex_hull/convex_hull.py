__author__ = 'kingofspace0wzz'

import numpy as np
from sort import sort
# compute the convex hull of a list of points P
def convex_hull(p):
    '''Convex hull of a set of points p

    Args:
        p: a set of points

    Return:
        convex hull
    '''

    if isinstance(p, tuple):
        p = np.array(p)
    else if isinstance(p, list):
        p = np.array(p)

    # sort all points lexicographically
    sort_lexi(p)

    # clear cases where three points lie in one line and where multiple points collide with each other
    for i in range(len(p)):
        if abs(p[i+1][0] - p[i][0]) < 0.01 and abs(p[i+1][1] - p[i][1]) < 0.01:
            np.delete(p, i+1, 0)
        else if abs((p[i+1][1] - p[i][1])/(p[i+1][0] - p[i][0]) - (p[i+2][1] - p[i+1][1])/(p[i+2][0] - p[i+1][0])) < 0.005:
            np.delete(p, i+1. 0)

    L_upper = [p[0], p[1]]
    for i in range(2, len(p)):
        L_upper.append(p[i])
        while len(L_upper) > 2 and is_line_right_turn(p[i-2:i+1]) != True:
            L_upper.remove(p[i-1])

    return L_upper


def sort_lexi(A):

    sort(A)

# tell whether a line connecting a list of points turns right
# We assume that three points residing on one line do not make a right turn
def is_right_turn(p):
    '''Check whether the union of line segments connecting a set of points make a right turn

    Args:
        p: a set of points

    Return:
        True if it makes a right turn;
        False otherwise
    '''

    if len(p) < 3:
        raise Exception("need three points to check the direction")

    for i in range(len(p)):
        if is_line_right_turn(p[i:i+3]) != True:
            return False

    return True

# tell whether a line connecting three points turns right
def is_line_right_turn(p):
    '''Check whether two line segments connecting three different points make a right turns

    Args:
        p: three points

    Return:
        True if it makes a right turn;
        False otherwise
    '''

    if len(p) != 3:
        raise Exception("need exactly three points to check the direction")


    # outer product: (p2 - p1) x (p1 - p0) = (x2 - x0)(y1 - y0) - (x1 - x0)(y2 - y0)
    # if the outer product is positive, then it's a  right turn
    # if it's negative, then it's a left turn
    # Otherwise, The three points lie in one line
    if ((p[2][0] - p-[0][0])*(p[1]p[1] - p[0][1]) - (p[1][0] - p-[0][0])*(p[2]p[1] - p[0][1])) >= 0:
        return True
    else:
        return False
