from math import sin, cos, pi, asin
import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.setx(-150)
t.sety(-150)
t.pendown()

screen = turtle.Screen()


def shape(s_length=200, sides=3):
    degrees = (sides - 2)*180
    t.color('black')
    for i in range(sides):
        t.forward(s_length)
        t.left(180-(degrees/sides))

def rad(deg):
    return deg*pi/180

def deg(rad):
    return rad*180/pi

def calc(S, F, sides=3):
    int_angle = (sides - 2)*180/sides
    G = sin(rad(int_angle)) * F
    I = cos(rad(int_angle)) * F
    J = S - F - I
    D = (J**2 + G**2)**(1/2)
    A = deg(asin(G/D))
    return A, D

def spiral(S, F, sides=3):
    while int(S) > F:
        shape(S, sides=sides)
        t.forward(F)
        A, S = calc(S, F, sides=sides)
        t.left(A)


L = 200
S = L
F = 10

spiral(S, F, sides=4)