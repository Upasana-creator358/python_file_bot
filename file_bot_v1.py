import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

from File_uploader_main import file_uploader

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def ask_gpt4_with_context(question, context, prompt):
    # Include context in the system message
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{prompt}. Context: {context}"},
            {"role": "user", "content": question},
        ],
        #max_tokens=500,  # Adjust for response length
        temperature=0.2,  # Adjust for randomness
    )
    return response.choices[0].message.content

# Sample Prompt for the assistant. Needs change 

st.write("""
# Python helper

This LLM is designed to take a file as an input and give a response based on the file.

Adding the file before asking the question will run the LLM, can't seem to figure out how to avoid that yet so stick to writing the question first then uploading the file
""")

prompt = """You are an expert in the python programming language. 
            Your task is to read, understand and explain code that you are given in a polite and respectful manner
            Do not make up things but do suggest changes if there is a problem or if the code can be optimised further
            If you do not have any input, introduce yourself and ask the user to provide code for you to analyse"""

# Initialising the context and questions. Here i am assuming the question is, explain this to me
question = "Explain this code and give me a analysis of what each section of the code does. If there are any erorrs show me where they are and show me ways of fixing the problem. Also, give me alternatives to fix or improve the code. Write out suggested code improvements"
context = str(file_uploader())

# Checking for 
def file_checker():
    if context == "":
        file_checker()
    elif prompt == "":
        raise RuntimeError("Prompt not found")
    else:
        st.write(ask_gpt4_with_context(context=context, question=question, prompt=prompt))

file_checker()