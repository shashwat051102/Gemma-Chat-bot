import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


# LangSmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# prompt template

prompt = ChatPromptTemplate(
    [
        # System basically means what i want my ai assistant to do
        ('system',"You are a helpful assistant please respond to the question asked"),
        ('user', 'Question{question}')
    ]
)

# Streamlit Framework

st.title('Langchain demo with Gemma model')
input_text = st.text_input("What question you have in your mind?")


# Ollama lamma2b model

llm=Ollama(model="gemma:2b")

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
