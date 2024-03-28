import os
import google.generativeai as genai
import textwrap
from dotenv import load_dotenv

class chatbot:

  def generate_response(self,query):

    load_dotenv()

    API_KEY= os.getenv("API_KEY")
    genai.configure(api_key=API_KEY)

    model= genai.GenerativeModel(model_name='gemini-pro')

    response=model.generate_content(query)

    text = response.text  
    text = text.replace('•', '  *')

    return textwrap.indent(text, '> ', predicate=lambda _: True)

