
import streamlit as st
import numpy as np


# Write directly to the app
st.title("ASK THE DOC APP")
st.sidebar.header("Specify ATTRIBUT")
selected_number = st.sidebar.text_input("Mission Number")
selected_type = st.sidebar.text_input("Mission type")
selected_location = st.sidebar.text_input("Mission location")
selected_client = st.sidebar.text_input("Client")
selected_category = st.sidebar.selectbox("Mission category", ["All","Contrats","CR","Cahier de charge","Devis/offres","Factures"])
with st.form('my_form'):
  query_text = st.text_input('Enter your question :', '')
  submitted = st.form_submit_button('Submit')

