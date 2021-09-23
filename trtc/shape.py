from .tuple import vector
from .matrix import Matrix
from .material import Material


class Shape():
    def __init__(self) -> None:
        self.transform = Matrix.identity_matrix()
        self.material = Material()

    def intersect(self, ray):
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def normal_at(self, p):
        local_point = self.transform.inverse() * p
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return world_normal.normalize()


class TestShape(Shape):

    def local_intersect(self, ray):
        self.saved_ray = ray

    def local_normal_at(self, p):
        return vector(p.x, p.y, p.z)
