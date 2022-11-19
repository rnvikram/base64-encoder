import streamlit as st
import base64

st.title("Base64 Encoder")

# st.header("Text to encode")
text_to_encode = st.text_area("Text to encode", value="")

ascii_encoded = text_to_encode.encode("ascii")

base64_encoded = base64.b64encode(ascii_encoded).decode("ascii")

st.header("Base64 encoded output")
st.text_area(value=base64_encoded, disabled=True)