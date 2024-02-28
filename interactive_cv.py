import streamlit as st
import numpy as np
import pandas as pd

st.title('Marc Grau Ortiz')
st.markdown('*Color Data Analyst*')
# Display graphical tools
st.sidebar.markdown('### Graphical and display options')
st.sidebar.markdown('**Text size**')
title_text_size = st.sidebar.slider(label='Please, select the text size:', min_value=10, max_value=100, value=16)
with st.sidebar.expander('About me', True):
    st.markdown('Astrophysicist who traded stars and galaxies for data analysis')
with st.expander('Experience', True):
    st.markdown('#### External IT Quality Technic (2017-2018): Tenea')
    st.markdown('- Validation of financial software in Windows environments')
    st.markdown('- Initial set up of computers in Windows environments')
    st.markdown('- Training of the new Junior roles')
    st.divider()
    st.markdown('#### Color Data Analyst (2021-): Venture Services')
    st.markdown('- colorimetric tests design and execution from scratch')
    st.markdown('- data cleaning, treatment and analysis of results to extract insights')
    st.markdown('- designed and implemented a *PowerBI*-like data analysis and visualization platform using Streamlit')
    st.markdown('- created and maintained a MySQL Database to structure large scale data')
with st.expander('Skills', True):
    st.info('Tip: numbers are indicative, by no means are an absolute grade of the listed skills')
    st.markdown('### :orange[General Python Tools]')
    skill_general_level = {'Pandas':80, 'Numpy':80, 'Streamlit':100, 'Jupyter Notebook':75}
    for sk, lv in skill_general_level.items():
        col1, col2 = st.columns(2)
        col1.markdown('*'+ sk + '*')
        lv_percentage = str(lv) + '%'
        col2.progress(value=lv, text=lv_percentage)
    st.divider()
    st.markdown('### :violet[Visualization Tools]')
    skill_vis_level = {'Plotly':90, 'Seaborn':50, 'Matplotlib':50}
    for sk, lv in skill_vis_level.items():
        col1, col2 = st.columns(2)
        col1.markdown('*'+ sk + '*')
        lv_percentage = str(lv) + '%'
        col2.progress(value=lv, text=lv_percentage)
    st.divider()
    st.markdown('### :blue[IDEs and more]')
    skill_tool_level = {'VS Code':75, 'MySQL':50, 'Github':60}
    for sk, lv in skill_tool_level.items():
        col1, col2 = st.columns(2)
        col1.markdown('*' + sk + '*')
        lv_percentage = str(lv) + '%'
        col2.progress(value=lv, text=lv_percentage)
    st.divider()
    st.markdown('### :green[Methodologies]')
    skill_met_level = {'Scrum':100}
    for sk, lv in skill_met_level.items():
        col1, col2 = st.columns(2)
        col1.markdown('*' + sk + '*')
        lv_percentage = str(lv) + '%'
        col2.progress(value=lv, text=lv_percentage)
with st.expander('Education', True):
    st.markdown("- **:green[2018-2019:]** Master's degree in Astrophysics, Cosmology and Particle Physics (University of Barcelona)")
    st.markdown("- **:green[2011-2017:]** Bachelor's degree in Pysics (University of Barcelona)")
with st.expander('Languages', True):
    st.markdown('- **Catalan:** Native')
    st.markdown('- **Spanish:** Native')
    st.markdown('- **English:** Upper-intermediate')
with st.sidebar.expander('Find me', True):
    st.markdown('- **:blue[Linkedin]:** @marcgror')
    st.markdown('- **Github:** https://github.com/marcgror')
with open("CV_Marc_Grau_Ortiz_2024.pdf", "rb") as file:
    pdfbyte = file.read()
    btn = st.sidebar.download_button('Download a PDF copy of the CV',
            data=pdfbyte,
            file_name="CV_Marc_Grau_Ortiz_2024.pdf",
            mime="application/octet-stream"
          )