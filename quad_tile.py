import turtle

from main import SavePosition, rspiral, lspiral, get_screen

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

t = get_screen()
quad_tile(t, S=120, F=10, rows=10, cols=10)

turtle.done()