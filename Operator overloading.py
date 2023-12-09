class Point(object):
    '''Represents a point in 2-D space.'''
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)
    def __add__(self,other):
        if isinstance(other, Point):
            return Point(self.x + other.x,self.y + other.y)
        elif isinstance(other, int):
            return Point(self.x + other,self.y + other)
