import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet='TestSheet')

st.dataframe(data)