from trtc.tuple import point, color
from trtc import Matrix, Canvas, utils
import math


if __name__ == "__main__":

    canvas_x = 800
    canvas_y = 800
    canvas_origin = point(canvas_x//2, 0, canvas_y//2)
    c = Canvas(canvas_x, canvas_y)
    face_color = color(1, 1, 0)

    twelve_o_clock = point(0, 0, 1)
    radius = 3/8 * canvas_x

    for clock_tick in range(1, 13):
        p = Matrix.identity_matrix()
        # Rotate around the y-axis 1/12 (pi/6) of a turn from the 
        # twelve o'clock position
        location = p.rotation_y(clock_tick * math.pi/6) * \
            twelve_o_clock * radius
        print(f'{clock_tick}: {location} ({round(location.x) + canvas_origin.x}, {round(location.z) + canvas_origin.z})')
        c.write_pixel(round(location.x) + canvas_origin.x,
                      round(location.z) + canvas_origin.z, face_color)

    utils.save_canvas("output/ch4.ppm", c)
