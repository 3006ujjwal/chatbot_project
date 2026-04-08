import streamlit as st
from chatbot import generate_response
from database import create_table, save_chat, load_chats

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 Intelligent Chatbot with Memory")

# Initialize DB
create_table()

# SESSION STATE
if "history" not in st.session_state:
    st.session_state.history = []   # EMPTY ON START

if "show_history" not in st.session_state:
    st.session_state.show_history = False

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.header("⚙️ Options")

    if st.button("📂 Load Previous Chats"):
        st.session_state.history = load_chats()
        st.session_state.show_history = True

    if st.button("🧹 Clear Current Chat"):
        st.session_state.history = []
        st.session_state.show_history = False

# ---------------- DISPLAY CHAT ---------------- #
if st.session_state.show_history:
    for user, bot in st.session_state.history:
        st.chat_message("user").write(user)
        st.chat_message("assistant").write(bot)

# ---------------- INPUT ---------------- #
user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)

    response = generate_response(user_input, st.session_state.history)

    st.chat_message("assistant").write(response)

    # Save to DB
    save_chat(user_input, response)

    # Update session only (not auto-load from DB)
    st.session_state.history.append((user_input, response))