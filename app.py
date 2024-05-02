import streamlit as st
import pandas as pd

st.title("Hello World")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)
