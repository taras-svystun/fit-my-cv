import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

from prompts import first_chatbot_message, chatbot_system_message


load_dotenv(".env")
URI = os.getenv("URI")
openai_api_key = os.getenv("OPENAI_API_KEY")

"# 💬 Chatbot for experience and background collection"
"🚀 A Streamlit chatbot powered by OpenAI"
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": first_chatbot_message}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-2024-05-13", messages=[{"role": "assistant", "content": chatbot_system_message}] + st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)