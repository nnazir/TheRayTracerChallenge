from .matrix import Matrix
from math import tan


class Camera():
    '''
    A camera that maps a 3D scene onto a 2D canvas
    '''

    def __init__(self, hsize, vsize, field_of_view, transform=Matrix.identity_matrix()) -> None:
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform
        self.pixel_size = None
        self._set_pixel_size()

    def _set_pixel_size(self):
        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize
