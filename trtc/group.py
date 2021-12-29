from .matrix import Matrix
from .shape import Shape
from .intersection import IntersectionList


class Group(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.transform = Matrix.identity_matrix()
        self.shapes = []

    def add_child(self, shape):
        shape.parent = self
        self.shapes.append(shape)

    def local_intersect(self, ray) -> IntersectionList:
        xs = IntersectionList()

        for shape in self.shapes:
            for i in shape.intersect(ray).intersections:
                xs.add(i)
        xs.sort_intersections()

        return xs
