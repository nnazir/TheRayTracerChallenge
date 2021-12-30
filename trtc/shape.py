"""
Shapes will be derived from the Shape class and used to determine
intersections with rays
"""

import uuid
from .tuple import vector
from .matrix import Matrix
from .material import Material
from abc import ABC


class Shape(ABC):
    """
    Abstract class for any shape to be derived from
    """

    def __init__(self) -> None:
        self.id = uuid.uuid4()
        self.transform = Matrix.identity_matrix()
        self.material = Material()
        self.parent = None

    def intersect(self, ray):
        """
        Returns the intersections of the ray with the shape.
        Calls the local_intersect of the derived shape
        """
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def normal_at(self, p):
        """ Returns the normal at a certain point """
        local_point = self.transform.inverse() * p
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()

    def world_to_object(self, p):
        """ Converts a world space point to object space """
        if self.parent:
            p = self.parent.world_to_object(p)
        return self.transform.inverse() * p

    def normal_to_world(self, normal):
        normal = self.transform.transpose().inverse() * normal
        normal.w = 0
        normal = normal.normalize()
        if self.parent:
            normal = self.parent.normal_to_world(normal)
        return normal


class TestShape(Shape):
    """
    A shape to be derived from Shape for testing only.
    """

    def __init__(self) -> None:
        super().__init__()
        self.saved_ray = None

    def local_intersect(self, ray):
        self.saved_ray = ray

    def local_normal_at(self, p):
        """ The normal_at function for the test shape """
        return vector(p.x, p.y, p.z)
