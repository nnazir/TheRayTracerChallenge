from .tuple import color
import textwrap


class Canvas():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.max_color = 255
        self.pixels = [[color(0, 0, 0)] * height for i in range(width)]
        self.canvas_header = f"P3\n{self.width} {self.height}\n{self.max_color}\n"

    def __rgb2ppm(self, pixel):
        t = round(pixel * self.max_color)
        if t > self.max_color:
            return self.max_color
        elif t < 0:
            return 0
        return t

    def write_pixel(self, x, y, color):
        self.pixels[x][y] = color

    def pixel_at(self, x, y):
        return self.pixels[x][y]

    def canvas_to_ppm(self):
        body = ""
        for h in range(self.height):
            line = ""
            for w in range(self.width):
                line += str(self.__rgb2ppm(self.pixel_at(w, h).red)) + ' '
                line += str(self.__rgb2ppm(self.pixel_at(w, h).green)) + ' '
                line += str(self.__rgb2ppm(self.pixel_at(w, h).blue)) + ' '
            if len(line) < 70:
                body += line.rstrip() + '\n'
            else:
                body += '\n'.join(textwrap.wrap(line, width=70)) + '\n'
        return self.canvas_header + body
