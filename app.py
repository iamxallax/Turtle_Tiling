from tempfile import NamedTemporaryFile
import random

import streamlit as st
from seaborn import color_palette
from matplotlib.colors import to_rgb, ListedColormap, LinearSegmentedColormap

from main import get_screen, CleanMove
from svg_turtle import SvgTurtle
from tri_tile import tri_tile
from quad_tile import quad_tile
from hex_tile import hex_tile
from octo_tile import oct_tile

with st.sidebar:

    t = get_screen()


    st.selectbox("Choose tiling", ['Triangle', 'Square', "Hexagon", 'Octogon'], key='tiling')

    st.slider('Side Length', min_value=10, max_value=300, value=120, step=1, key='len')
    st.slider('Step (\% of Side Length)', min_value=1, max_value=32, value=8, step=1, key='step')
    st.slider('Rows', min_value=1, max_value=20, value=10, step=1, key='rows')
    st.slider('Columns', min_value=1, max_value=20, value=10, step=1, key='cols')
    # st.color_picker('Start Color', '#000000', key='scol')
    # st.color_picker('End Color', '#000000', key='ecol')
    if 'colordict' not in st.session_state:
        st.session_state.colordict = {'col' + str(i): '#000000' for i in range(5)}
    
    if "randomize_idx" not in st.session_state:
        st.session_state.randomize_idx = None

    # st.markdown(
    #     """
    #     <style>
    #     input[type="check"] {
    #         width: 32px !important;
    #         height: 20px !important;
    #         padding: 0 !important;
    #         border-radius: 8px !important;
    #         border: 2px solid #dee2e6 !important;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    if not st.checkbox('Use Seaborn Palette', value=True):
        cols = st.columns(3)
        for z in range(5):
            for i, col in enumerate(cols):
                with col:
                    with st.container():
                        picker_key = f"col{z}"
                        # If flag set, set value in state **before** widget!
                        if i == 1:
                            if st.session_state.randomize_idx == z:
                                random_color = '#%06X' % random.randint(0, 0xFFFFFF)
                                st.session_state.colordict[picker_key] = random_color
                                st.session_state.randomize_idx = None # Reset after use
                            st.session_state[picker_key] = st.session_state.colordict[picker_key]

                        if i == 0:
                            st.checkbox('Use color?', value=False if z > 1 else True, key='check'+str(z))
                        if st.session_state['check'+str(z)] and i == 1:
                            st.color_picker('color' + str(z), st.session_state.colordict[picker_key], key=picker_key, label_visibility="collapsed")
                        if st.session_state['check'+str(z)] and i == 2:
                            if st.button('Random', key='rand'+str(z)):
                                st.session_state.randomize_idx = z
                                st.rerun()
        
        url = st.text_input('Colors from coolors.io')
        if url:
            colors = url.split('/')[-1].split('-')
            if len(colors) == 5:
                for i, color in enumerate(colors):
                    st.session_state.colordict['col' + str(i)] = '#' + color
                url = None
                st.rerun()

        palette = LinearSegmentedColormap.from_list('custom_palette', list(map(to_rgb, list(st.session_state['col' + str(i)] for i in range(5) if st.session_state['check' + str(i)]))) + [(0, 0, 0)], N=256)
    else:
        st.selectbox('palette', ['icefire', 'mako', 'rocket', 'magma', 'inferno', 'plasma', 'viridis', 'cividis', 'cubehelix', "crest", "flare", "vlag", "mako"], key='palette')
        palette = color_palette(st.session_state.palette, as_cmap=True)

    # scol = tuple(int(st.session_state.scol[i:i+2], 16) for i in (1, 3, 5))
    # ecol = tuple(int(st.session_state.ecol[i:i+2], 16) for i in (1, 3, 5))
    if st.session_state.tiling == 'Triangle':
        tri_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, colormap=palette, rows=st.session_state.rows, cols=st.session_state.cols)
    if st.session_state.tiling == 'Square':
        quad_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, colormap=palette, rows=st.session_state.rows, cols=st.session_state.cols)
    if st.session_state.tiling == 'Hexagon':
        hex_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, colormap=palette, rows=st.session_state.rows, cols=st.session_state.cols)
    if st.session_state.tiling == 'Octogon':
        oct_tile(t, S=st.session_state.len, F=(st.session_state.len / 100) * st.session_state.step, colormap=palette, rows=st.session_state.rows, cols=st.session_state.cols)

    with NamedTemporaryFile('w+') as f:
        t.save_as(f.name)
        f.flush()
        st.session_state.img = f.read()

st.image(st.session_state.img)