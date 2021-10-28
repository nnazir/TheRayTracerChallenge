from .tuple import point, vector
from .utils import EPSILON


class Intersection():
    def __init__(self, t, object) -> None:
        self.t = t
        self.object = object

    def __lt__(self, other):
        return self.t < other.t

    def prepare_computations(self, ray):
        # Instantiate a data structure for storing some precomputed values
        comps = Computations()
        # Copy the intersection's properties, for convenience
        comps.t = self.t
        comps.object = self.object
        # Precompute some useful values
        comps.point = ray.position(comps.t)
        comps.eyev = -ray.direction
        comps.normalv = comps.object.normal_at(comps.point)
        
        if comps.normalv.dot(comps.eyev) < 0:
            comps.inside = True
            comps.normalv = -comps.normalv
        else:
            comps.inside = False        
        comps.over_point = comps.point + comps.normalv * EPSILON
        comps.reflectv = ray.direction.reflect(comps.normalv)

        return comps


class IntersectionList():
    def __init__(self, *argv) -> None:
        self.count = len(argv)
        self.intersections = [a for a in argv]
        self.intersections.sort()

    def add(self, item):
        self.intersections.append(item)
        self.count = len(self.intersections)

    def sort_intersections(self):
        list.sort(self.intersections, key=lambda i: i.t)

    def hit(self):
        '''
        Assumes the list of intersections are sorted. Returns the lowest positive intersection.
        '''
        for i in self.intersections:
            if i.t > 0:
                return i


class Computations():
    def __init__(self) -> None:
        self.t = 0
        self.object = None
        self.point = point(0, 0, 0)
        self.eyev = vector(0, 0, 0)
        self.normalv = vector(0, 0, 0)
        self.inside = None
        self.over_point = point(0, 0, 0)
