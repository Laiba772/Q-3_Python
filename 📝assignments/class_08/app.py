import streamlit as st
import sqlite3
from datetime import datetime

# Initialize SQLite connection
conn = sqlite3.connect('mental_health.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mood_logs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        mood TEXT,
        note TEXT,
        date TEXT
    )
''')
conn.commit()

# Companion response logic
def get_companion_response(mood):
    if mood == "happy":
        return "😊 I'm glad you're feeling happy today!"
    elif mood == "sad":
        return "😔 I'm here for you. Want to talk about it?"
    elif mood == "angry":
        return "😤 Take a deep breath. Want to try a calming exercise?"
    else:
        return "🤔 Thanks for sharing your feelings."

# UI
st.title("🧠 Mental Health Tracker")
st.subheader("Daily Mood Check-In")

name = st.text_input("Your Name")
mood = st.selectbox("How are you feeling today?", ["happy", "sad", "angry", "neutral"])
note = st.text_area("Add a note (optional)")

if st.button("Submit"):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO mood_logs (name, mood, note, date) VALUES (?, ?, ?, ?)', 
                   (name, mood, note, date))
    conn.commit()
    response = get_companion_response(mood)
    st.success("Entry saved!")
    st.info(response)

# View Logs
st.markdown("---")
st.subheader("📖 Your Mood History")
cursor.execute('SELECT * FROM mood_logs ORDER BY date DESC')
rows = cursor.fetchall()
for row in rows:
    st.markdown(f"**{row[1]}** ({row[4]}): *{row[2]}* — {row[3]}")
