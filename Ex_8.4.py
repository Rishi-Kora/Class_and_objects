class Point(object):
    '''Represents a point in 2-D space.'''
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)

class Rectangle(object):
    def __init__(self,corner_x = 0.0,corner_y = 0.0,width = 10.0,height = 10.0):
        self.width = width
        self.height = height
        self.corner = Point(corner_x,corner_y)
    def __str__(self):
        return "(%.2f,%.2f)%.2f x %.2f"%(self.corner.x,self.corner.y,self.width,self.height)
