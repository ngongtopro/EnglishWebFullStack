import streamlit as st
import requests


# Sửa URL cho API
url = "http://127.0.0.1:8000/chatbot/chatbot_api"


st.title("Demo Chatbot")

if "messages" not in  st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        data = {
            "role": "user",
            "content": prompt
        }
        response = requests.post(url, json=data)
        print(response.status_code)
        print(response.request.method)
        # curl -X POST http://127.0.0.1:8000/chatbot/chatbot_api -H "Content-Type: application/json" -d '{"role": "user", "content": "Test message"}'
        full_res = ""
        if response.status_code == 200:
            print(response.json())
            full_res = response.json().get("content", "Content rỗng.")
        else:
            full_res = f"Error: {response.status_code} - {response.text}"
        st.markdown(full_res)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_res
        }
    )