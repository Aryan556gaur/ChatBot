import streamlit as st
from chatbot import chatbot
    
def main():
    st.set_page_config("QA with Aryan")
    
    st.header("ChatBot")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Just finishing up..."):

            object = chatbot()
            response =object.generate_response(user_question)
                
            st.write(response)
                
                
if __name__=="__main__":
    main()          