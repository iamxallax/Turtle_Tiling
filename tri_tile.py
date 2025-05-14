from svg_turtle import SvgTurtle
from seaborn import color_palette

from main import SavePosition, rspiral, lspiral, get_screen, CleanMove

def tri_row(t, S, F, colormap, cols=1):
    for c in range(cols):
        with SavePosition(t):
            with CleanMove(t):
                t.forward(c * S)
            lspiral(t, S, F, colormap)
            t.left(60)
            rspiral(t, S, F, colormap)
    
def tri_tile(t, S, F, colormap, rows=1, cols=1):
    for r in range(rows):
        tri_row(t, S, F, colormap, cols)
        with CleanMove(t):
            rotate = 120 if r % 2 == 0 else 60
            t.left(rotate)
            t.forward(S)
            t.right(rotate)
 

if __name__ == "__main__":
    t = SvgTurtle(500, 500)
    tri_tile(t, S=120, F=10, colormap=color_palette('flare', as_cmap=True), rows=20, cols=20)
    t.save_as('image.svg')