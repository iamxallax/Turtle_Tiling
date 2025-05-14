import turtle

from main import SavePosition, rspiral, lspiral, get_screen, CleanMove

def oct_tile(t, S, F, colormap, rows=10, cols=2):
    for col in range(cols):
        with SavePosition(t):
            for row in range(rows):
                lspiral(t, S, F, colormap, sides=8)
                t.forward(S)
                with SavePosition(t):
                    t.right(45)
                    lspiral(t, S, F, colormap, sides=4)
                    rspiral(t, S, F, colormap, sides=4)
                t.forward(S * (2 ** (1/2)))
        with CleanMove(t):
            t.left(90)
            t.forward((2 * S / (2 ** (1/2))) + S)
            t.right(90)
                