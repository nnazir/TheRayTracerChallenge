import math
from trtc.utils import EPSILON
from trtc.tuple import vector
from trtc.shape import Shape
from trtc.intersection import Intersection, IntersectionList


class Cube(Shape):
    def local_intersect(self, ray):
        xtmin, xtmax = self.check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = self.check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = self.check_axis(ray.origin.z, ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        if tmin > tmax:
            return IntersectionList()

        return IntersectionList(Intersection(tmin, self), Intersection(tmax, self))

    def check_axis(self, origin, direction):
        tmin_numerator = -1 - origin
        tmax_numerator = 1 - origin

        if abs(direction) >= EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * math.inf
            tmax = tmax_numerator * math.inf

        if tmin > tmax:
            tmin, tmax = tmax, tmin

        return tmin, tmax

    def local_normal_at(self, p):
        maxc = max(abs(p.x), abs(p.y), abs(p.z))
        if maxc == abs(p.x):
            return vector(p.x, 0, 0)
        elif maxc == abs(p.y):
            return vector(0, p.y, 0)
        return vector(0, 0, p.z)