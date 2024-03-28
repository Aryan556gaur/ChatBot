import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import textwrap

load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

def chat(user_message):
  """
  Sends user message to Gemini Pro and returns its response

  Args:
      user_message: Text from the user

  Returns:
      String: Response from Gemini Pro
  """

  model = genai.GenerativeModel(model_name='gemini-pro')
  chat_session = model.start_chat()

  response = chat_session.send_message(user_message)
  text = response.text  
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

response_area = st.empty()

st.title("Chatbot")
user_input = st.text_input("You:")
if user_input:
    response = chat(user_input)
    response_area.text(f"Gemini Pro: {response}")

