from trtc.matrix import Matrix
from trtc.shape import Shape


class Group(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.transform = Matrix.identity_matrix()
        self.shapes = []
