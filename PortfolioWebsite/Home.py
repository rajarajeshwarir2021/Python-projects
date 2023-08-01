import pandas as pd
import streamlit as st


st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Raji")
    content = """
    This is my demo Portfolio Website. I am an Associate Engineer with interests in Python, AI, 
    DataScience, and MLOps.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", delimiter=';')

with col3:
    for idx, row in df[:1].iterrows():
        st.header(row['Title'])
        st.write(row['Description'])
        st.image("images/" + row['Image'])
        st.write(f"[SourceCode]({row['Url']})")

with col4:
    for idx, row in df[1:].iterrows():
        st.header(row['Title'])
        st.write(row['Description'])
        st.image("images/" + row['Image'])
        st.write(f"[SourceCode]({row['Url']})")