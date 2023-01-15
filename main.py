from math import sin, cos, pi, asin
import turtle
import time
import itertools

class SavePosition:
    def __init__(self, t):
        self.heading = t.heading()
        self.position = t.position()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t.penup()
        t.setheading(self.heading)
        t.setposition(self.position)
        t.pendown()


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

def lspiral(t, S, F, sides=3):
    with SavePosition(t):
        while int(S) > F:
            shape(t, S, sides=sides)
            t.forward(F)
            A, S = calc(S, F, sides=sides)
            t.left(A)

def rspiral(t, S, F, sides=3):
    angle = (sides - 2)*180 / sides
    with SavePosition(t):
        while int(S) > F:
            shape(t, S, sides=sides)
            t.forward(S - F)
            A, S = calc(S, F, sides=sides)
            t.left(180 - angle - A)

def make_tri(t, S, rows, cols):
    height = S * sin(rad(60))
    coords = []
    #(x, y, heading, spiral(r/l))
    for c in range(cols):
        for r in range(rows):
            x = c * S
            y = r * height
            if r % 2 == 1:
                heading = 120
            else:
                heading = 0
            


def tri_row(t, S, F, cols=1):
    for c in range(cols):
        with SavePosition(t):
            t.forward(c * S)
            lspiral(t, S, F)
            t.left(60)
            rspiral(t, S, F)
    
def tri_tile(t, S, F, rows=1, cols=1):
    for r in range(rows):
        with SavePosition(t):
            tri_row(t, S, F, cols)
        t.penup()
        t.left(120)
        t.forward(S)
        t.pendown()
        t.right(120)

def quad_tile(t, S, F, rows=1, cols=1):
    for r in range(rows):
        for c in range(cols):
            with SavePosition(t):
                t.forward(c * S)
                if (r + c) % 2 == 0:
                    lspiral(t, S, F, sides=4)
                else:
                    rspiral(t, S, F, sides=4)
        t.setposition(t.xcor(), t.ycor() + S)

def hex_tile(t, S, F, cols=1):
    for c in range(cols):
        with SavePosition(t):
            t.right(120)
            t.forward(S)
            lspiral(t, S, F)
        with SavePosition(t):
            t.left(120)
            t.forward(S)
            t.right(60)
            rspiral(t, S, F)
        with SavePosition(t):
            lspiral(t, S, F, sides=6)
            t.right(120)
            rspiral(t, S, F, sides=6)
        t.forward(S)
        with SavePosition(t):
            rspiral(t, S, F)
            t.right(60)
            lspiral(t, S, F)
        t.forward(S)

def circle(t, S=0.5):
    shape(t, S, sides=1000)

screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(n=0, delay=None)
# t.color('black')
t.penup()
t.goto((-1000, -1000))

S = 100
F = 10

screen.colormode(255)

quad_tile(t, S, F, 200, 200)