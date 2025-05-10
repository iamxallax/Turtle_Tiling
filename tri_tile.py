from svg_turtle import SvgTurtle

from main import SavePosition, rspiral, lspiral, get_screen

def tri_row(t, S, F, scol, ecol, cols=1):
    for c in range(cols):
        with SavePosition(t):
            t.forward(c * S)
            lspiral(t, S, F, scol, ecol)
            t.left(60)
            rspiral(t, S, F, scol, ecol)
    
def tri_tile(t, S, F, scol, ecol, rows=1, cols=1):
    for r in range(rows):
        tri_row(t, S, F, scol, ecol, cols)
        t.penup()
        rotate = 120 if r % 2 == 0 else 60
        t.left(rotate)
        t.forward(S)
        t.pendown()
        t.right(rotate)


if __name__ == "__main__":
    t = SvgTurtle(500, 500)
    tri_tile(t, S=120, F=10, rows=20, cols=20)
    t.save_as('image.svg')