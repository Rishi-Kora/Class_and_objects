class Point(object):
    '''Represents a point in 2-D space.'''
def get_euclidean_dist(p1,p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
