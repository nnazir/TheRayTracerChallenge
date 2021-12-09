import math
from .utils import float_equal, EPSILON
from .tuple import vector
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

        xs = IntersectionList()

        if not float_equal(a, 0):

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

            y0 = ray.origin.y + t0 * ray.direction.y
            if self.minimum < y0 < self.maximum:
                xs.add(Intersection(t0, self))

            y1 = ray.origin.y + t1 * ray.direction.y
            if self.minimum < y1 < self.maximum:
                xs.add(Intersection(t1, self))

        self.intersect_caps(ray, xs)
        return xs

    def local_normal_at(self, p):
        # compute teh square of the distance from the y axis
        dist = p.x**2 + p.z**2

        if dist < 1 and p.y >= self.maximum - EPSILON:
            return vector(0, 1, 0)
        elif dist < 1 and p.y <= self.minimum + EPSILON:
            return vector(0, -1, 0)
        return vector(p.x, 0, p.z)

    def check_cap(self, ray, t):
        '''
        A helper function to reduce duplication.
        Checks to see if the intersection at 't' is within a radius
        of 1 (the radius of your cylinders) from the y axis.
        '''
        x = ray.origin.x + t * ray.direction.x
        z = ray.origin.z + t * ray.direction.z
        return (x**2 + z**2) <= 1

    def intersect_caps(self, ray, xs):
        # caps only matter if the cylinder is closed, and might possibly be
        # intersected by the ray.
        if self.closed is False or float_equal(ray.direction.y, 0):
            return

        # check for an intersection with the lower end cap by intersecting
        # the ray with the plane at y=self.minimum
        t = (self.minimum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.add(Intersection(t, self))

        # check for an intersection with the upper end cap by intersecting
        # the ray with the plane at y=self.maximum
        t = (self.maximum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.add(Intersection(t, self))
