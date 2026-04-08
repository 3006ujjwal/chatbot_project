import streamlit as st
import cohere

co = cohere.Client(st.secrets["COHERE_API_KEY"])

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