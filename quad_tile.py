from svg_turtle import SvgTurtle

from main import SavePosition, rspiral, lspiral, get_screen

def quad_tile(t, S, F, scol, ecol, rows=1, cols=1):
    for r in range(rows):
        for c in range(cols):
            with SavePosition(t):
                t.forward(c * S)
                if (r + c) % 2 == 0:
                    lspiral(t, S, F, scol, ecol, sides=4)
                else:
                    rspiral(t, S, F, scol, ecol, sides=4)
        t.setposition(t.xcor(), t.ycor() + S)

if __name__ == "__main__":
    t = get_screen()
    quad_tile(t, S=120, F=10, rows=10, cols=10)
    t.save_as('image.svg')