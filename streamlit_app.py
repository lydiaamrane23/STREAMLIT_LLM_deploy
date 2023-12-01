import orchest
import streamlit as st


import orchest
import weaviate


def get_weaviate_client():
   
    auth_config = weaviate.AuthApiKey(api_key="test")
    return weaviate.Client(
   url = "http://weaviate:8080",  # Replace with your endpoint
   auth_client_secret=auth_config,
   additional_headers = {
         "X-OpenAI-Api-Key": "test"  # Replace with your inference API key
     }
 )


def define_schema():

    client = get_weaviate_client()
    client.schema.delete_all()
    client.schema.get()  # get the full schema as example

    schema = {
        "classes": [
            {
                "class": "Author",
                "description": "The writer of a comments",
                "properties": [
                    {
                        "dataType": ["string"],
                        "description": "Name of the author",
                        "name": "name",
                    },
                    {
                        "dataType": ["Comment"],
                        "description": "Comments this author wrote",
                        "name": "writtenComments",
                    },
                ],
            },
            {
                "class": "Comment",
                "description": "A written comment, by an author",
                "properties": [
                    {
                        "dataType": ["text"],
                        "description": "The content of the comment",
                        "name": "content",
                    },
                    {
                        "dataType": ["text"],
                        "description": "Permalink to the comment.",
                        "name": "permalink",
                    },
                    {
                        "dataType": ["date"],
                        "description": "The date of when the comment was written",
                        "name": "date",
                    },
                ],
            },
        ]
    }

    client.schema.create(schema)
client = get_weaviate_client()

query = st.text_input("Zoek door comments", key="query")

if len(query) > 0:
    content = {
        "concepts": [query],
    }

    result = (
        client.query.get("Comment", ["content", "date", "permalink"])
        .with_near_text(content)
        .with_limit(10)
        .do()
    )

    comments = result["data"]["Get"]["Comment"]

    if comments is None:
        st.write("Did not find any comments.")
    else:
        for comment in comments:
            st.markdown("[" + comment["date"] + "]("+comment["permalink"]+")")
            st.markdown(comment["content"])
            st.markdown("---")
