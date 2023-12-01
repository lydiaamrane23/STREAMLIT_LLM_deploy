import streamlit as st
from langchain.llms import OpenAI

import weaviate

openai_api_key ="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"

## replace EMBEDDEDOPTION BY THIS WHEN i Wwill have information
#auth_config = weaviate.AuthApiKey(api_key="test")
#url = "http://weaviate:8080",  # Replace with your endpoint
#auth_client_secret=auth_config,

client = weaviate.Client(
    embedded_options=weaviate.EmbeddedOptions(),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)
from langchain.vectorstores import Weaviate



# define input structure
client.schema.delete_all()
client.schema.get()
schema = {
    "classes": [
        {
            "class": "Chatbot",
            "description": "Documents for chatbot",
            "vectorizer": "text2vec-openai",
            "moduleConfig": {"text2vec-openai": {"model": "ada", "type": "text"}},
            "properties": [
                {
                    "dataType": ["text"],
                    "description": "The content of the paragraph",
                    "moduleConfig": {
                        "text2vec-openai": {
                            "skip": False,
                            "vectorizePropertyName": False,
                        }
                    },
                    "name": "content",
                },
            ],
        },
    ]
}

client.schema.create(schema)
vectorstore = Weaviate(client, "Chatbot", "content", attributes=["source"])

st.title('🦜🔗 Quickstart App')

openai_api_key ="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" 

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # retrieve text related to the query
    docs = vectorstore.similarity_search(input_text)
    st.info("ok",docs)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)


