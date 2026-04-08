import cohere
import streamlit as st

co = cohere.Client(st.secrets["fquAbMdkbSB9AosOpzt46no6oUglf103fqFDBQtO"])

def generate_response(user_input, history):
    
    formatted_history = ""
    
    for user, bot in history:
        formatted_history += f"User: {user}\nBot: {bot}\n"
    
    prompt = f"""
You are an intelligent chatbot.

Conversation so far:
{formatted_history}

User: {user_input}
Bot:
"""

    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )

    return response.text.strip()