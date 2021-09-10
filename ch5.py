from trtc.matrix import Matrix
from trtc.ray import Ray
from trtc.sphere import Sphere
from trtc.tuple import color, point
from trtc import Canvas, utils
from math import pi

if __name__ == "__main__":

    # start the ray at z = -5
    ray_origin = point(0, 0, -5)

    # put the wall at z = 10
    wall_z = 10

    wall_size = 7.0

    canvas_pixels = 800
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = Canvas(canvas_pixels, canvas_pixels)
    c = color(1, 0, 0)  # red
    shape = Sphere()
    # shrink it along the y axis
    # shape.transform = Matrix.scaling(1, 0.5, 1)
    # shrink it along the x axis
    # shape.transform = Matrix.scaling(0.5, 1, 1)
    # shrink it, and rotate it!
    # shape.transform = Matrix.rotation_z(pi / 4) * Matrix.scaling(0.5, 1, 1)
    # shrink it, and skew it!
    shape.transform = Matrix.shearing(
        1, 0, 0, 0, 0, 0) * Matrix.scaling(0.5, 1, 1)

    # for each fow of pixels in the canvas
    for y in range(0, canvas_pixels-1):
        # compute the world y coordinate (top = +half, bottom = -half)
        world_y = half - pixel_size * y

        # for each pixel in the row
        for x in range(0, canvas_pixels-1):
            # compute the world x coordinate (left = -half, right = half)
            world_x = -half + pixel_size * x

            # describe the point on the wall that the ray will target
            position = point(world_x, world_y, wall_z)
            r = Ray(ray_origin, (position - ray_origin).normalize())
            xs = shape.intersect(r)
            if xs.hit():
                canvas.write_pixel(x, y, c)

    utils.save_canvas("output/ch5-4.ppm", canvas)
