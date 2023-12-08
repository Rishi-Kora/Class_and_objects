class Point(object):
    '''Reperesents apoint in 2-D Space.'''
class Rectangle(object):
    '''Represents a rectangle.'''
    def find_centre(self):
        p = Point()
        p.x = self.corner.x + self.width/2.0
        p.y = self.corner.y + self.height/2.0
        return p
