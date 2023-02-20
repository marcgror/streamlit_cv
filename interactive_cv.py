import streamlit as st
import numpy as np
import pandas as pd

st.title('Marc Grau Ortiz')
with st.expander('About me', True):
    st.markdown('Physicist moving to Data Science/Analysis and Machine Learning. Comfortable with Python and Linux, always trying to learn new uses for AI and ways for applying it to solve real-life problems. Recently in love with Tableau.')
with st.expander('Experience', True):
    st.markdown('### External IT Quality Technic (2017-2018)')
    st.markdown('- Validation of financial software in Windows environments')
    st.markdown('- Initial set up of computers in Windows environments')
    st.markdown('- Training of the new Junior roles')
with st.expander('Skills', True):
    st.markdown('### Python')
    skill_level = {'Pandas':80, 'Numpy':80, 'Streamlit':100}
    for sk, lv in skill_level.items():
        col1, col2 = st.columns(2)
        col1.markdown('**'+ sk + '**')
        lv_percentage = str(lv) + ' %'
        col2.progress(value=lv)
with st.expander('Education', True):
    st.markdown("- **2018-2019:** Master's degree in Astrophysics, Cosmology and Particle Physics (Universitat of Barcelona)")
    st.markdown("- **2011-2017:** Bachelor's degree in Pysics (Universitat of Barcelona)")

with st.expander('Languages', True):
    st.markdown('- **Catalan:** Native')
    st.markdown('- **Spanish:** Native')
    st.markdown('- **English:** Upper-intermediate')
with st.expander('Find me', True):
    st.markdown('- **Linkedin:** @marcgror')
    st.markdown('- **Github:** https://github.com/marcgror')