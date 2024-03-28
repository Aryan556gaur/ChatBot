import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import textwrap
from socketio import Client

# Initialize SocketIO client
sio = Client()
sio.connect('http://localhost:5000')

class Chatbot:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name='gemini-pro')

    def generate_response(self, query):
        response = self.model.generate_content(query)
        text = response.text.replace('•', '  *')
        formatted_text = textwrap.indent(text, '> ', predicate=lambda _: True)
        return formatted_text

# Create a chatbot instance
chatbot = Chatbot()

# Streamlit app
st.title('Real-Time Chatbot')

# Input box for user query
user_query = st.text_input('Enter your message:')

# Send message button
if st.button('Send'):
    if user_query:
        # Send user query to server
        sio.emit('message', user_query)

# Receive and display chatbot response
@st.cache(allow_output_mutation=True)
def receive_response():
    return []

messages = receive_response()

@sio.on('response')
def receive_message(message):
    messages.append(message)
    st.text_area('Chatbot Response:', '\n'.join(messages), height=200, max_chars=None, key='response')

# Run the Streamlit app
if __name__ == '__main__':
    st.set_page_config(layout='wide')
    st.write('Open this URL in your browser: http://localhost:8501')
    st.write('Enter your messages in the input box and click "Send". The chatbot response will appear below.')
    st.write('(Note: Make sure the SocketIO server is running on port 5000)')
