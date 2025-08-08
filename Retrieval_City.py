import streamlit as st
#from vertexai.generative_models import GenerativeModel, Part
#from vertexai.language_models import TextEmbeddingModel

from langchain_google_vertexai import VertexAI, VertexAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from pprint import pprint
import os
import vertexai

vertexai.init(project="city-rag1", location="us-central1")
@st.cache_resource
def Vertex1():
    Document2 = TextLoader("City_CurrentSeason2.txt").load()

    Document3 =  RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20).split_documents(Document2)

    # Initialize the embedding model
    Embedding_model = VertexAIEmbeddings(model_name="gemini-embedding-001")

    database2= Chroma.from_documents(Document3, embedding=Embedding_model)
    return database2


def Summary_x(Query2,database2):
    llm2 = VertexAI(model_name="gemini-2.0-flash")
    docs=database2.similarity_search(Query2, k=5)
    context1 = "\n\n".join([doc.page_content for doc in docs])

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", "You are an expert football analyst. Summarize the following information about Manchester City's 2024-25 season based only on the provided context. Be concise and highlight key aspects like league position, key players, players injuries, and overall performance. do not include information which is not in the context."),
        ("human", "Context: {context}\n\nQuery: {query}"),
        ])


    Lang_chain = prompt_template | llm2 | StrOutputParser()

    Summary = Lang_chain.invoke({"context": context1, "query": Query2})
    return Summary


st.title("Manchester City 2024-25 Season Summary")
st.write("Enter a query to get a summary of Manchester City's season based on provided data.")

user_query = st.text_input("Enter your query:", "Summarize Manchester City's 2024-25 EPL season performance and the role of their best player")

if st.button("Generate Summary"):
    if user_query:
        with st.spinner("Generating summary..."):
            try:
                database2 = Vertex1()
                summary_text = Summary_x(user_query,database2)
                st.success("Summary generated!")
                st.write(summary_text)
            except Exception as e1:
                st.error(f"Error occurred: {e1}")
    else:
        st.warning("Please enter the Query")

