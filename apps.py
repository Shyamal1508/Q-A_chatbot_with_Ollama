import streamlit as st
import openai
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=str(os.getenv("LANGCHAIN_API_KEY"))
os.environ["LANGCHAIN_TRACKING_V2 "]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A chatbot with ollama"

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.please response to the user queries"),
        ("user","question:{question}")
    ]

)
def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

##title of app
st.title("enhanced Q&A chatbot with ollama")
st.sidebar.title("settings")
llm=st.sidebar.selectbox("select the language model",["gemma:2b"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max tokens",min_value=50,max_value=200,value=100)

st.write("go ahead and ask any question")
user_input=st.text_input("question:")

if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("please respond the query")





