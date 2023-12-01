import streamlit as st
import openai
import os
#from openai import AsyncOpenAI
from openai import OpenAI

st.title("Artelia LLM Chat v02")

openai.api_key = "vide"
os.environ['OPENAI_API_KEY'] = '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'
openai.api_base = os.getenv("OPENAI_API_BASE")

# Set a default model
if "model" not in st.session_state:
    st.session_state["model"] = os.getenv("MODEL")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up at Artelia?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
       

    st.session_state.messages.append({"role": "assistant", "content": "kaka"})
