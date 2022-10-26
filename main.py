from math import sin, cos, pi, asin
import turtle
import time

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
t.speed(3)
turtle.tracer(n=0, delay=None)
t.color('black')

S = 150
F = 10
t.pendown()

def hextile(t, S, F):
    for i in range(6):
        t.left(60)
        if i % 2 == 0:
            lspiral(t, S, F)
        else:
            rspiral(t, S, F)
        
hextile(t, S, F)
for i in range(6):
    with SavePosition(t):
        t.setheading(i * 60)
        t.penup()
        t.forward(S * 1.5)
        t.left(90)
        t.forward(S * sin(rad(60)))
        t.right(30)
        t.pendown()
        hextile(t, S, F)



#t.penup()
#t.setposition(-200, -200)
#t.pendown()
#make_triangles(t, S, F, rows=2, cols=4)
    
#coords = make_grid(S, 4, 6)

#for x, y, inverted in coords:
#    t.penup()
#    t.setx(x)
#    t.sety(y)
#    t.pendown()
#    spiral(t, S, F, sides=4, inverted=inverted)
#    turtle.update()
#    time.sleep(0.25)
