from trtc import point, Matrix, Tuple
import trtc
from trtc.intersection import Intersection, IntersectionList
import uuid
import math


class Sphere():
    def __init__(self) -> None:
        self.id = uuid.uuid4()
        self.transform = Matrix.identity_matrix()

    def intersect(self, ray):
        ray2 = ray.transform(self.transform.inverse())

        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is center at the world origin
        sphere_to_ray = ray2.origin - point(0, 0, 0)
        a = ray2.direction.dot(ray2.direction)
        b = 2 * ray2.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b*b - 4 * a * c

        if discriminant < 0:
            return IntersectionList()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        if t1 < t2:
            return IntersectionList(Intersection(t1, self),
                                    Intersection(t2, self))
        else:
            return IntersectionList(Intersection(t2, self),
                                    Intersection(t1, self))

    def normal_at(self, world_point):
        object_point = self.transform.inverse() * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return Tuple.normalize(world_normal)
