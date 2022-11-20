import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Base64 Encoder")

components.html('<meta name="google-site-verification" content="NZPyZ5mCaOB88Fdv740bFgdNJa-3abZke9uJnawf7Ic" />')

st.title("Base64 Encoder")
st.subheader("Free tool base64 encode text online")

text_to_encode = st.text_area("Text to encode", value="")

ascii_encoded = text_to_encode.encode("ascii")

base64_encoded = base64.b64encode(ascii_encoded).decode("ascii")

st.text_area("Base64 encoded output", value=base64_encoded, disabled=True)

st.subheader("Safe and secure")
st.caption("All communications with our servers come through secure SSL encrypted connections (https).")
st.subheader("Completely free")
st.caption("Our tool is free to use. From now on, you don't need to download any software for such simple tasks.")