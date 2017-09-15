__author__ = 'kingofspace0wzz'


#------------------------------------------------------
# two simple checking-direction functions, the parameters of which are a set of points
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
    if direction(p) >= 0:
        return True
    else:
        return False

def direction(p):

    if len(p) != 3:
        raise Exception("need exactly three points to check the direction")

    return (p[2][0] - p-[0][0])*(p[1]p[1] - p[0][1]) - (p[1][0] - p-[0][0])*(p[2]p[1] - p[0][1])


def segment_intersect(p):
    '''Check if two lines intersect

    Args:
        p: a set of four points, each pair of which represents a lines

    Return:
        True if two lines intersect
        False Otherwise
    '''
    if len(p) != 4:
        raise Exception("need 4 points")

    d0 = direction([p[2],p[3],p[0]])
    d1 = direction([p[2],p[3],p[1]])
    d2 = direction([p[0],p[1],p[2]])
    d3 = direction([p[0],p[1],p[3]])

    # if d0 * d1 < 0 and d2 * d3 < 0:
    if ((d0 > 0 and d1 < 0) or (d0 < 0 and d1 > 0)) and ((d2 > 0 and d3 < 0) or (d2 < 0 and d3 > 0)):
        return True
    elif d0 == 0 and on_segment(p[2],p[3],p[0]):
        return True
    elif d1 == 0 and on_segment(p[2],p[3],p[1]):
        return True
    elif d2 == 0 and on_segment(p[0],p[1],p[2]):
        return True
    elif d3 == 0 and on_segment(p[0],p[1],p[3]):
        return True
    else:
        return False

def on_segment(p1, p2, p3):
    '''Check whether p3 lies in between p1 and p2'''

    if min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1]):
        return True
    else:
        return False
