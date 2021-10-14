import math
from trtc import vector, point
from trtc.intersection import Intersection, IntersectionList
from trtc.material import Material
from trtc.shape import Shape


class Sphere(Shape):

    def local_intersect(self, ray):
        # ray2 = ray.transform(self.transform.inverse())

        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is center at the world origin
        sphere_to_ray = ray.origin - point(0, 0, 0)
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return IntersectionList()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        if t1 < t2:
            return IntersectionList(Intersection(t1, self),
                                    Intersection(t2, self))

        return IntersectionList(Intersection(t2, self),
                                Intersection(t1, self))

    def local_normal_at(self, world_point):
        return vector(world_point.x, world_point.y, world_point.z)
