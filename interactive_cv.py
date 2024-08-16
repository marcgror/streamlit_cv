import streamlit as st
st.set_page_config(page_title='Marc Grau Ortiz', page_icon=':page_facing_up:', layout='wide')

st.title(body=':blue[Marc Grau Ortiz]')
st.markdown(':blue[*Data Analyst | Python | SQL*]')
with st.expander('About me', True):
    st.subheader(body=':blue[About me]', divider='blue')
    st.markdown("I develop PowerBI/Tableau-like Data Analysis and Visualization platforms using Python. They allow users to interact with the data and apply filters in real time to get the analysis that best suits their needs. \
                I love to work with SQL databases, structuring the data in order to optimize its storage and subsequent access.")
    st.markdown("I am currently continuing my education with courses and certifications as I intend to evolve more towards a Data Engineer profile, touching on topics such as Cloud Computing.")
    st.markdown("I consider myself very structured and organized when programming, commenting and documenting code whenever I can to make it easier to read and understand.\
                I like to tackle challenges one at a time in order to be 100% focused on what I'm doing.")
with st.expander('Experience', True):
    st.subheader(body=':blue[Experience]', divider='blue')
    st.markdown('#### External IT Quality Technic (2017-2018): Tenea')
    st.markdown('- Validation of financial software in Windows environments')
    st.markdown('- Initial set up of computers in Windows environments')
    st.markdown('- Training of the new Junior roles')
    st.divider()
    st.markdown('#### Data Analyst (2021-): Venture Services')
    st.markdown('- data cleaning, treatment and analysis of data to extract insights')
    st.markdown('- designed and implemented a *Tableau/PowerBI*-like data analysis and visualization platform using *Streamlit*')
    st.markdown('- created and maintained a *MySQL* Database to structure large scale data')
    st.markdown('- reporting of results to aid in decision making')
with st.expander('Skills', True):
    st.subheader(body=':blue[Skills]', divider='blue')
    st.info('Tip: numbers are indicative, by no means are an absolute grade of the listed skills')
    col_general, col_space_1, col_vis, col_space_2, col_tool, col_space_3, col_met = st.columns([4,1,4,1,4,1,4])
    with col_general:
        st.markdown('### :orange[General Python Tools]:computer:')
        skill_general_level = {'Pandas':80, 'Numpy':80, 'Streamlit':100, 'Jupyter Notebook':75}
        for sk, lv in skill_general_level.items():
            col1, col2 = st.columns([1,2])
            col1.markdown('*'+ sk + '*')
            lv_percentage = str(lv) + '%'
            col2.progress(value=lv, text=lv_percentage)
    with col_vis:
        st.markdown('### :violet[Visualization Tools]:chart_with_upwards_trend:')
        skill_vis_level = {'Plotly':90, 'Seaborn':50, 'Matplotlib':50}
        for sk, lv in skill_vis_level.items():
            col1, col2 = st.columns([1,2])
            col1.markdown('*'+ sk + '*')
            lv_percentage = str(lv) + '%'
            col2.progress(value=lv, text=lv_percentage)
    with col_tool:
        st.markdown('### :blue[IDEs and more]:notebook:')
        skill_tool_level = {'VS Code':75, 'SQL':50, 'Github':60}
        for sk, lv in skill_tool_level.items():
            col1, col2 = st.columns([1,2])
            col1.markdown('*' + sk + '*')
            lv_percentage = str(lv) + '%'
            col2.progress(value=lv, text=lv_percentage)
with col_met:
        st.markdown('### :green[Methodologies]:handshake:')
        skill_met_level = {'Scrum':100}
        for sk, lv in skill_met_level.items():
            col1, col2 = st.columns([1,2])
            col1.markdown('*' + sk + '*')
            lv_percentage = str(lv) + '%'
            col2.progress(value=lv, text=lv_percentage)
with st.expander('Education', True):
    st.subheader(body=':blue[Education]', divider='blue')
    st.markdown("- **:green[2018-2019:]** Master's degree in Astrophysics, Cosmology and Particle Physics (University of Barcelona)")
    st.markdown("- **:green[2011-2017:]** Bachelor's degree in Pysics (University of Barcelona)")
with st.expander('Languages', True):
    st.subheader(body=':blue[Languages]', divider='blue')
    st.markdown('- **Catalan:** Native')
    st.markdown('- **Spanish:** Native')
    st.markdown('- **English:** Upper-intermediate')
with st.sidebar.expander('Find me', True):
    st.markdown('- **:blue[Linkedin]:** @marcgror')
    st.markdown('- **Github:** https://github.com/marcgror')
    st.markdown('- marcgrauortiz@outlook.es')
    st.markdown('- 647271168')
with open("CV_Marc_Grau_Ortiz_2024.pdf", "rb") as file:
    pdfbyte = file.read()
    btn = st.sidebar.download_button('Download a PDF copy of the CV',
            data=pdfbyte,
            file_name="CV_Marc_Grau_Ortiz_2024.pdf",
            mime="application/octet-stream"
          )