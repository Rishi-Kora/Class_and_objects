class Point(object):
    '''Represents a point in 2-D space.'''
    def __init__(self,x = 0.0,y = 0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f,%.2f)" %(self.x, self.y)
        
