from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')
user_input = st.text_input("Enter your prompt")
model = ChatOpenAI(model="gpt-4o-mini_v2024-07-18")

if st.button("Summarise"):
    result = model.invoke(user_input)
    st.write(result.content)
