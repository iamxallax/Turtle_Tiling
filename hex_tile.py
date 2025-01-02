from svg_turtle import SvgTurtle

from main import SavePosition, rspiral, lspiral, get_screen, CleanMove


def hex_tile(t, S, F, rows, cols):
    t.dot(10)
    for r in range(rows):
        with SavePosition(t):
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
        with CleanMove(t):
            t.left(90)
            t.forward((S * (3 ** (1/2)) * 2))
            t.right(90)



if __name__ == "__main__":
    t = get_screen()
    hex_tile(t, S=120, F=10, cols=10)
    t.save_as('image.svg')