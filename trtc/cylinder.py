import math
from .utils import float_equal
from .tuple import point, vector
from .ray import Ray
from .shape import Shape
from .intersection import Intersection, IntersectionList


class Cylinder(Shape):
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

        return IntersectionList(Intersection(t0, self), Intersection(t1, self))

    def local_normal_at(self, p):
        return vector(p.x, 0, p.z)
