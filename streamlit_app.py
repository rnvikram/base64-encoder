import streamlit as st
import base64

st.title("Base64 Encoder")
st.subheader("Free tool base64 encode text online")

text_to_encode = st.text_area("Text to encode", value="")

ascii_encoded = text_to_encode.encode("ascii")

base64_encoded = base64.b64encode(ascii_encoded).decode("ascii")

st.text_area("Base64 encoded output", value=base64_encoded, disabled=True)

st.subheader("Safe and secure")
st.caption("All communications with our servers come through secure SSL encrypted connections (https). We delete uploaded files from our servers immediately after being processed and the resulting downloadable file is deleted right after the first download attempt or 15 minutes of inactivity (whichever is shorter). We do not keep or inspect the contents of the submitted data or uploaded files in any way. Read our privacy policy below for more details.")
st.subheader("Completely free")
st.caption("Our tool is free to use. From now on, you don't need to download any software for such simple tasks.")