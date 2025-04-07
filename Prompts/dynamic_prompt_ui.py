from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini_v2024-07-18")

st.header('Reasearch Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
                           "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", [
                           "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", [
                            "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt("prompts/template.json")


# Dictionary of input variables
# input_variables = ['paper_input', style_input, length_input]

if st.button('Summarize'):
    # chaining
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    # prompt = template.invoke({
    #     "paper_input": paper_input,
    #     "style_input": style_input,
    #     "length_input": length_input
    # })

# result = model.invoke(prompt)
    st.write(result.content)
