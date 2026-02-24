import streamlit as st
import requests

st.title("Chatgpt clone using Gemini APIs")
st.set_page_config(page_title="Chat1.0")

#define API
API_URL = "http://127.0.0.1:8000/ask"

#initialize session state for list of messages
if "messages" not in st.session_state:
    st.session_state.messages = []

#if session state already contains messsages, display those using streamlit's chat component
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#handle input 
if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #make api call and get the /ask REST API
    question = prompt
    full_response = ""
    with st.chat_message("assistant"):
        #make api call here
        with requests.post(API_URL, data = {"question": question}) as r:
            json_response = r.json()
            response = json_response['response']
            print(f"JSON response: {json_response}")
            print(f"Sending to FE: {response}")
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})