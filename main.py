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

def make_grid(S=200, rows=2, cols=4):
    coords = []
    inverted = True
    for r in range(rows):
        for c in range(cols):
            xpos = ((c - 1) * S) - ((int(cols / 2) - 1) * S)
            ypos = ((r - 1) - (int(rows / 2) - 1)) * S
            if c == 0 and r != 0:
                if cols % 2 == 0:
                    inverted = inverted
                else:
                    inverted = not inverted
            else:
                inverted = not inverted
            coords.append((xpos, ypos, inverted))
    return coords

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.color('black')

S = 150
F = 10

#1, 1(-400, 0)
#1, 2(-200, 0)
#1, 3(0, 0)
#1, 4(200, 0)

#2, 1(-400, -200)
#2, 2(-200, -200)
#2, 3(0, -200)
#2, 4(200, -200)

coords = make_grid(S, 4, 4)

for x, y, inverted in coords:
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    spiral(t, S, F, sides=4, inverted=inverted)
