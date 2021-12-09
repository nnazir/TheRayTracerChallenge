import math
from .shape import Shape
from .intersection import Intersection, IntersectionList


class Cone(Shape):

    def local_intersect(self, ray) -> IntersectionList:
        a = ray.direction.x**2 - ray.direction.y**2 + ray.direction.z**2

        b = 2 * ray.origin.x * ray.direction.x - \
            2 * ray.origin.y * ray.direction.y + \
            2 * ray.origin.z * ray.direction.z

        c = ray.origin.x**2 - ray.origin.y**2 + ray.origin.z**2

        # ray misses
        if a == 0 and b == 0:
            return IntersectionList()

        if a == 0 and b != 0:
            t = -c/(2*b)
            return IntersectionList(Intersection(t, self))

        disc = b**2 - 4 * a * c

        # ray does not intersect the cylinder
        if disc < 0:
            return IntersectionList()

        t0 = (-b - math.sqrt(disc)) / (2 * a)
        t1 = (-b + math.sqrt(disc)) / (2 * a)

        return IntersectionList(Intersection(t0, self),
                                Intersection(t1, self))
