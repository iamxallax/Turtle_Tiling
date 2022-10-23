from math import sin, cos, pi, asin
import turtle

def rad(deg):
    return deg*pi/180


def deg(rad):
    return rad*180/pi
    

def shape(t, S=200, sides=3, inverted=False):
    degrees = (sides - 2)*180
    for i in range(sides):
        t.forward(S)
        if inverted:
            t.right(180-(degrees/sides))
        else:
            t.left(180-(degrees/sides))

def calc(S, F, sides=3):
    int_angle = (sides - 2)*180/sides
    G = sin(rad(int_angle)) * F
    I = cos(rad(int_angle)) * F
    J = S - F - I
    D = (J**2 + G**2)**(1/2)
    A = deg(asin(G/D))
    return A, D

def spiral(t, S, F, sides=3, inverted=False):
    if inverted:
        t.penup()
        t.setheading(90)
        t.forward(S)
        t.pendown()
        t.setheading(0)
    while int(S) > F:
        shape(t, S, sides=sides, inverted=inverted)
        t.forward(F)
        A, S = calc(S, F, sides=sides)
        if inverted:
            t.right(A)
        else:
            t.left(A)
    t.setheading(0)

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.color('black')

S = 200
F = 10

coords = [(0, 0, True), (0, -200, False), (-200, -200, True), (-200, 0, False), (-400, 0, True), (-400, -200, False), (200, -200, True), (200, 0, False)]

#def make_grid(S, rows=2, cols=4):

for x, y, inverted in coords:
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    spiral(t, S, F, sides=4, inverted=inverted)
