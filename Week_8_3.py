class Point(object):
    '''Reperesents apoint in 2-D Space.'''
class Rectangle(object):
    '''Represents a rectangle.'''
def find_top_right(Rect):
    p = Point()
    p.x = Rect.corner.x + Rect.width
    p.y = Rect.corner.y + Rect.height
    return p
    
