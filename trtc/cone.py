import math
from .utils import float_equal, EPSILON
from .tuple import vector
from .shape import Shape
from .intersection import Intersection, IntersectionList


class Cone(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.minimum = float('-inf')
        self.maximum = float('inf')
        self.closed = False

    def local_intersect(self, ray) -> IntersectionList:
        xs = IntersectionList()

        a = ray.direction.x**2 - ray.direction.y**2 + ray.direction.z**2

        b = 2 * ray.origin.x * ray.direction.x - \
            2 * ray.origin.y * ray.direction.y + \
            2 * ray.origin.z * ray.direction.z

        c = ray.origin.x**2 - ray.origin.y**2 + ray.origin.z**2

        # ray misses
        # if a == 0 and b == 0:
        if float_equal(a, 0) and float_equal(b, 0):
            return xs

        # if a == 0 and b != 0:
        if float_equal(a, 0) and not float_equal(b, 0):
            t = -c/(2*b)
            xs.add(Intersection(t, self))
            return xs

        disc = b**2 - 4 * a * c

        # ray does not intersect the cone
        if disc < 0:
            return IntersectionList()

        disc_root = math.sqrt(disc)
        t0 = (-b - disc_root) / (2 * a)
        t1 = (-b + disc_root) / (2 * a)

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

    def check_cap(self, ray, t, y=0):
        x = ray.origin.x + t * ray.direction.x
        z = ray.origin.z + t * ray.direction.z
        return (x**2 + z**2) <= y**2

    def intersect_caps(self, ray, xs):
        # caps only matter if the cylinder is closed, and might possibly be
        # intersected by the ray.
        if not self.closed or float_equal(ray.direction.y, 0):
            return xs

        # check for an intersection with the lower end cap by intersecting
        # the ray with the plane at y=self.minimum
        t0 = (self.minimum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t0, self.minimum):
            xs.add(Intersection(t0, self))

        # check for an intersection with the upper end cap by intersecting
        # the ray with the plane at y=self.maximum
        t1 = (self.maximum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t1, self.maximum):
            xs.add(Intersection(t1, self))

    def local_normal_at(self, p):
        # compute the square of the distance from the y axis
        dist = p.x**2 + p.z**2

        if dist < 1 and p.y >= self.maximum - EPSILON:
            return vector(0, 1, 0)
        elif dist < 1 and p.y <= self.minimum + EPSILON:
            return vector(0, -1, 0)

        y = math.sqrt(p.x**2 + p.z**2)
        if y > 0 and p.y > 0:
            y = -y

        return vector(p.x, y, p.z)
