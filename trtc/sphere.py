from trtc import point
import uuid
import math


class Sphere():
    def __init__(self) -> None:
        self.id = uuid.uuid4()

    def intersect(self, ray):
        # the vector from the sphere's center, to the ray origin
        # remember: the sphere is center at the world origin
        sphere_to_ray = ray.origin - point(0, 0, 0)
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b*b - 4 * a * c

        if discriminant < 0:
            return

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        if t1 < t2:
            return (t1, t2)
        else:
            return (t2, t1)