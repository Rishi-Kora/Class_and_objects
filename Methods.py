class Point(object):
    '''Represents a point in 2-D space.'''
    def move(self,width,height):
        self.x += width
        self.y += height
