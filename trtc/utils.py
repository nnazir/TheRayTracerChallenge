EPSILON = 0.00001


def float_equal(a, b):
    return abs(a - b) < EPSILON

def save_canvas(file, canvas):
    with open(file, "w") as f:
        f.write(canvas.canvas_to_ppm())