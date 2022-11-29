import streamlit as st

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

nav_to("https://drive.google.com/uc?export=download&id=1uqaxwNltil3OsGvn8sgzYQ9t6s9Br1Wp")
