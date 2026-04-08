import sqlite3

DB_NAME = "chat_history.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        bot_response TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def save_chat(user_input, bot_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO chats (user_input, bot_response) VALUES (?, ?)",
        (user_input, bot_response)
    )
    
    conn.commit()
    conn.close()

def load_chats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT user_input, bot_response FROM chats")
    rows = cursor.fetchall()
    
    conn.close()
    return rows