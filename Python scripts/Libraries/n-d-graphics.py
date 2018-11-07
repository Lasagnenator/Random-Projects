#n-dimensional projection

class DimensionError(ValueError):pass

class Point(object):
    def __init__(self, coordinates):
        self.dimensions = len(coordinates)
        self.coordinates = coordinate
    def project(self, plane, focal_point):
        """plane is a list of coordinates (reverse) specifying the dimension to project to.
focal_point is the coordinate of the camera must be the same dimension as plane
    -> also reversed.
Cannot project to 0 dimensions. This will raise DimensionError."""
        if len(plane)!=len(focal_point):
            raise ValueError('focal_point does not have the same dimensionality as the plane of projection')
        if len(plane)>=self.dimensions:
            raise DimensionError('Trying to project to too few dimensions.')
        dimensions = len(plane)
        t = 1
        
        for i in range(dimensions):
            pass
        

"""
a_1 = t*p_1+f_1
a_2 = t*p_2+f_1
...
a_n = t*p_n+f_n
a_n is the new coordinates.
p_1 is the original coordinate
Solve for t when a_n is fixed.
Substitute t into every other value and get the new value of a_1...a_n
Remove a_n from the list.
Replace p_n with a_n.
Repeat for how ever many dimensions are needed.
"""



hypercube = [1,1,1,1], [1,1,1,-1], [1,1,-1,1], [1,1,-1,-1], [1,-1,1,1], [1,-1,1,-1], [1,-1,-1,1], [1,-1,-1,-1], [-1,1,1,1], [-1,1,1,-1], [-1,1,-1,1], [-1,1,-1,-1], [-1,-1,1,1], [-1,-1,1,-1], [-1,-1,-1,1], [-1,-1,-1,-1]
