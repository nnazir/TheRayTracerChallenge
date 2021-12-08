import math
from .utils import float_equal
from .tuple import point, vector
from .ray import Ray
from .shape import Shape
from .intersection import Intersection, IntersectionList


class Cylinder(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.minimum = float('-inf')
        self.maximum = float('inf')
        self.closed = False

    def local_intersect(self, ray) -> IntersectionList:
        a = ray.direction.x**2 + ray.direction.z**2

        # ray is parallel to the y axis
        if float_equal(a, 0):
            return IntersectionList()

        b = 2 * ray.origin.x * ray.direction.x + \
            2 * ray.origin.z * ray.direction.z

        c = ray.origin.x**2 + ray.origin.z**2 - 1
        disc = b**2 - 4 * a * c

        # ray does not intersect the cylinder
        if disc < 0:
            return IntersectionList()

        t0 = (-b - math.sqrt(disc)) / (2 * a)
        t1 = (-b + math.sqrt(disc)) / (2 * a)

        if t0 > t1:
            t0, t1 = t1, t0

        xs = IntersectionList()
        y0 = ray.origin.y + t0 * ray.direction.y
        if self.minimum < y0 < self.maximum:
            xs.add(Intersection(t0, self))

        y1 = ray.origin.y + t1 * ray.direction.y
        if self.minimum < y1 < self.maximum:
            xs.add(Intersection(t1, self))

        # return IntersectionList(Intersection(t0, self), Intersection(t1, self))
        return xs

    def local_normal_at(self, p):
        return vector(p.x, 0, p.z)
