from trtc.tuple import point, vector, color
from trtc import Canvas
from trtc.utils import save_canvas


class projectile():
    def __init__(self, p, v) -> None:
        self.position = p
        self.velocity = v


class environment():
    def __init__(self, g, w) -> None:
        self.gravity = g
        self.wind = w


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)


def run_loop(c, p, e):
    count = 0
    while p.position.y > 0:
        count += 1
        x = round(p.position.x)
        y = c.height - round(p.position.y)
        p = tick(e, p)
        print(f'[{count}] {p.velocity}, {p.position}')
        if p.position.y < c.height-1:
            c.write_pixel(x, y, color(1, 0, 0))


if __name__ == "__main__":

    start = point(0, 1, 0)
    velocity = vector(1, 3, 0).normalize() * 11.25
    p = projectile(start, velocity)

    gravity = vector(0, -0.1, 0)
    wind = vector(-0.01, 0, 0)
    e = environment(gravity, wind)

    c = Canvas(900, 550)

    run_loop(c, p, e)
    save_canvas('output/ch2.ppm', c)