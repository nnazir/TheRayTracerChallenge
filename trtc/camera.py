from .tuple import point
from .matrix import Matrix
from .ray import Ray
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

    def ray_for_pixel(self, px, py):
        '''
        Compute the world coordinates at the center of the given pixel
        and then construct a ray that passes throught that point.
        '''
        # the offset from the edge of the canvas to the pixel's center
        xoffset = (px+0.5) * self.pixel_size
        yoffset = (py+0.5) * self.pixel_size

        # the untransformed coordinates of the pixel in world space.
        # (remember that the camera looks toward -z, so +x s to the *left*.)
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        # using the camera matrix, transform the canvas point and the origin,
        # and then compute the ray's direction vector.
        # (remember that the canvas is a z=-1)
        pixel = self.transform.inverse() * point(world_x, world_y, -1)
        origin = self.transform.inverse() * point(0, 0, 0)
        direction = (pixel - origin).normalize()

        return Ray(origin, direction)
