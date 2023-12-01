
import streamlit as st
import numpy as np
import weaviate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
openai_key = "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"

client = weaviate.Client(
    embedded_options=weaviate.EmbeddedOptions(),
    additional_headers={
        "X-OpenAI-Api-Key": openai_key
    }
)
vectorstore = Weaviate(client, "Chatbot", "content", attributes=["source"])



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
# retrieve text related to the query
docs = vectorstore.similarity_search(query_text)
if submitted:
  chain = load_qa_chain(
    OpenAI(openai_api_key ="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",temperature=0), 
    chain_type="stuff")
  # create answer
  st.info(chain.run(input_documents=docs, question=query))
  



