# Turtle Tiling

This is a program that makes cool patterns using Turtle and Python.

Here are some screenshots.

## Triangular tiling:

```python
import turtle

from main import SavePosition, rspiral, lspiral, get_screen

def tri_row(t, S, F, cols=1):
    for c in range(cols):
        with SavePosition(t):
            t.forward(c * S)
            lspiral(t, S, F)
            t.left(60)
            rspiral(t, S, F)
    
def tri_tile(t, S, F, rows=1, cols=1):
    for r in range(rows):
        tri_row(t, S, F, cols)
        t.penup()
        rotate = 120 if r % 2 == 0 else 60
        t.left(rotate)
        t.forward(S)
        t.pendown()
        t.right(rotate)

t = get_screen()
tri_tile(t, S=120, F=10, rows=10, cols=10)

turtle.done()
```
![tri_tile](tri_tile.png "Tri tile")

## Square tiling:

```python
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
```

![quad_tile](quad_tile.png "Quad tile")

## Hexagonal tiling:

```python
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
```

![hex_tile](Hex_tile.png "Hex tile")