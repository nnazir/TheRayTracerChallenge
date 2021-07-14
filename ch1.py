from trtc.tuple import point, vector

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


def run_loop(p, e):
    count = 0
    while p.position.y > 0:
        count += 1
        p = tick(e, p)
        print(f'[{count}] {p.velocity}, {p.position}')


if __name__ == "__main__":
    # projectile starts one unit above the origin,
    # velocity is normalized to 1 unit/tick.
    p = projectile(point(0, 1, 0), vector(1, 1, 0).normalize())

    # gravity -0.1 unit/tick, and wind is -0.01 unit/tick
    e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

    run_loop(p, e)

    # Initial velocity x 2
    p = projectile(point(0, 1, 0), vector(1, 1, 0).normalize() * 2)
    e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    run_loop(p, e)

    # Initial velocity x 3
    p = projectile(point(0, 1, 0), vector(1, 1, 0).normalize() * 3)
    e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    run_loop(p, e)
