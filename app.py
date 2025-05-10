from tempfile import NamedTemporaryFile

import streamlit as st

from main import get_screen, CleanMove
from svg_turtle import SvgTurtle
from tri_tile import tri_tile
from quad_tile import quad_tile
from hex_tile import hex_tile

with st.sidebar:

    t = get_screen()


    st.selectbox("Choose tiling", ['Triangle', 'Square', "Hexagon"], key='tiling')

    st.slider('Side Length', min_value=10, max_value=300, value=120, step=1, key='len')
    st.slider('Step (\% of Side Length)', min_value=1, max_value=32, value=8, step=1, key='step')
    st.slider('Rows', min_value=1, max_value=20, value=10, step=1, key='rows')
    st.slider('Columns', min_value=1, max_value=20, value=10, step=1, key='cols')
    st.color_picker('Start Color', '#000000', key='scol')
    st.color_picker('End Color', '#000000', key='ecol')


    st.session_state.scol = tuple(int(st.session_state.scol[i:i+2], 16) for i in (1, 3, 5))
    st.session_state.ecol = tuple(int(st.session_state.ecol[i:i+2], 16) for i in (1, 3, 5))
    if st.session_state.tiling == 'Triangle':
        tri_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, scol=st.session_state.scol, ecol=st.session_state.ecol, rows=st.session_state.rows, cols=st.session_state.cols)
    if st.session_state.tiling == 'Square':
        quad_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, scol=st.session_state.scol, ecol=st.session_state.ecol, rows=st.session_state.rows, cols=st.session_state.cols)
    if st.session_state.tiling == 'Hexagon':
        hex_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, scol=st.session_state.scol, ecol=st.session_state.ecol, rows=st.session_state.rows, cols=st.session_state.cols)

    with NamedTemporaryFile('w+') as f:
        t.save_as(f.name)
        f.flush()
        st.session_state.img = f.read()

st.image(st.session_state.img)