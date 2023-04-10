import turtle

from main import SavePosition, rspiral, lspiral, get_screen


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

t = get_screen()
hex_tile(t, S=120, F=10, cols=10)

turtle.done()