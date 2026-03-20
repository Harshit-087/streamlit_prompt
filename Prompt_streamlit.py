from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt  # use to create dynamic prompt (PromptTemplate)

load_dotenv()


model = ChatOpenAI(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    base_url="https://api.groq.com/openai/v1"   
    )

st.header("Research Tool")


paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
       
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

#  loading the template  file
template = load_prompt("template.json")

# filling the placeholder in the template (mapping)
prompt = template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})

if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)