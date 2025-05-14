from math import sin, cos, pi, asin, ceil
from svg_turtle import SvgTurtle
import seaborn as sns
import numpy as np
from numpy import astype

class CleanMove:
    def __init__(self, t):
        self.t = t

    def __enter__(self):
       self.t.penup()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t.pendown()

class SavePosition:
    def __init__(self, t):
        self.t = t

        self.heading = t.heading()
        self.position = t.position()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with CleanMove(self.t):
            self.t.setheading(self.heading)
            self.t.setposition(self.position)


def rad(deg):
    return deg*pi/180


def deg(rad):
    return rad*180/pi

    
def shape(t, S=200, sides=3):
    degrees = (sides - 2)*180
    for i in range(sides):
        t.forward(S)
        t.left(180-(degrees/sides))


def calc(S, F, sides=3):
    int_angle = (sides - 2)*180/sides
    G = sin(rad(int_angle)) * F
    I = cos(rad(int_angle)) * F
    J = S - F - I
    D = (J**2 + G**2)**(1/2)
    A = deg(asin(G/D))
    return A, D


def lspiral(t, S, F, colormap, sides=3):
    color_steps = ceil(S / F)
    # Calculate the normalized values to sample the colormap
    # indices = [i / (color_steps - 1) for i in range(color_steps)]
    # # Get RGB tuples (in range 0-255) from the colormap
    # colors = [tuple(int(255 * c) for c in colormap(val)[:3]) for val in indices]
    colors = list(map(list, map(lambda x: map(lambda x: int(x * 255), x), list(colormap(np.linspace(0, 1, color_steps))))))


    with SavePosition(t):
        step = 1
        while int(S) > F:
            # Use the corresponding precomputed color
            cur_color = colors[min(step, len(colors) - 1)]
            t.color(f'#{cur_color[0]:02X}{cur_color[1]:02X}{cur_color[2]:02X}')
            shape(t, S, sides=sides)
            t.forward(F)
            A, S = calc(S, F, sides=sides)
            t.left(A)   
            step += 1


def rspiral(t, S, F, colormap, sides=3):
    color_steps = ceil(S / F)
    angle = (sides - 2) * 180 / sides

    # Generate color samples from the colormap
    # indices = [i / (color_steps - 1) for i in range(color_steps)]
    # colors = [tuple(int(255 * c) for c in colormap(val)[:3]) for val in indices]
    colors = list(map(list, map(lambda x: map(lambda x: int(x * 255), x), list(colormap(np.linspace(0, 1, color_steps))))))
    # colors = list(
    #     map(list, map(
    #         lambda x: int(255 * x), colormap(
    #             np.linspace(0, 1, color_steps)))))

    with SavePosition(t):
        step = 0
        while int(S) > F:
            cur_color = colors[min(step, len(colors) - 1)]
            t.color(f'#{cur_color[0]:02X}{cur_color[1]:02X}{cur_color[2]:02X}')
            shape(t, S, sides=sides)
            t.forward(S - F)
            A, S = calc(S, F, sides=sides)
            t.left(180 - angle - A)
            step += 1

def circle(t, S=0.5):
    shape(t, S, sides=1000)


def get_screen():
    t = SvgTurtle(1000, 1000)
    with CleanMove(t):
        t.goto((-500, -500))
    return t