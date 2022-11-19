import streamlit as st
"""Hello world"""



text_to_encode = st.text_area("Text to encode", value="")

ascii_encoded = text_to_encode.encode("ascii")

base64.b64encode(ascii_encoded)