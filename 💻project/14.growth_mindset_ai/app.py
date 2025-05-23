# growth_mindset_app.py
import streamlit as st
import requests
from io import BytesIO
import re
from fpdf import FPDF

# Page config
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱")
st.title("🌱 Growth Mindset AI")

# Quote function
def get_daily_quote():
    try:
        res = requests.get("https://zenquotes.io/api/today")
        if res.status_code == 200:
            data = res.json()
            return f"“{data[0]['q']}” – {data[0]['a']}"
        return "Unable to fetch quote today."
    except:
        return "Error fetching quote. You're still amazing—keep pushing forward!"

# Strip emojis for PDF
def strip_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text or '')

# PDF generation
def create_pdf(challenge, reflection, achievement, quote):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_text_color(34, 139, 34)
    pdf.cell(200, 10, txt="Growth Mindset Journal Summary", ln=True, align='C')
    pdf.set_text_color(0, 0, 0)

    pdf.multi_cell(0, 10, f"Challenge:\n{strip_emojis(challenge)}\n")
    pdf.multi_cell(0, 10, f"Reflection:\n{strip_emojis(reflection)}\n")
    pdf.multi_cell(0, 10, f"Achievement:\n{strip_emojis(achievement)}\n")
    pdf.multi_cell(0, 10, f"Quote of the Day:\n{strip_emojis(quote)}\n")
    pdf.multi_cell(0, 10, "Remember: Embrace challenges. Learn from failures. Keep growing!")

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return BytesIO(pdf_bytes)

# Welcome message
st.header("👋 Welcome To Your Growth Journey!")
st.write("✨ Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app supports your growth mindset through reflection, challenges, and achievements!")

# Quote section
st.header("💡 Today's Growth Mindset Quote")
quote = get_daily_quote()
st.success(quote)

# Challenge section
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("💭 Share your challenge or goal for today:")
if user_input:
    st.success(f"🚀 Challenge accepted: **{user_input}**. You’ve got this!")
else:
    st.warning("⚠️ Share a challenge to get started!")

# Reflection section
st.header("📝 Reflect on Your Journey")
reflection_input = st.text_area("🪞 How has your growth been lately?")
if reflection_input:
    st.success("🧠 Insight noted! Reflection is powerful.")
else:
    st.info("💭 Take a moment to reflect and write it down.")

# Achievement section
st.header("🏆 Celebrate Your Achievements")
achievement_input = st.text_input("🎉 Share a win, big or small:")
if achievement_input:
    st.success("👏 Great work! Celebrate every step.")
else:
    st.info("🥳 Even small wins matter—share one!")

# Progress Tracker
st.header("📊 Your Progress Tracker")
progress = 0
if user_input:
    progress += 1
if reflection_input:
    progress += 1
if achievement_input:
    progress += 1

st.progress(progress / 3)

if progress == 3:
    st.balloons()
    st.success("🌟 You’ve completed all sections today! Keep up the momentum.")
elif progress == 2:
    st.info("✅ Almost there! Just one more section to fill.")
elif progress == 1:
    st.info("🔄 Great start! Try completing more sections.")
else:
    st.info("🕊️ Start your growth by sharing your thoughts!")

# Download journal
if progress > 0:
    st.header("📄 Download Your Journal Summary")
    pdf_file = create_pdf(user_input, reflection_input, achievement_input, quote)
    st.download_button(
        label="📥 Download PDF",
        data=pdf_file,
        file_name="growth_mindset_journal.pdf",
        mime="application/pdf"
    )

# Footer
st.markdown("---")
st.markdown("### 🌟 Stay Inspired")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📧 Contact")
    st.markdown("📬 rajlaiba65@gmail.com")

with col2:
    st.markdown("#### 🔗 Connect")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/laiba-rajput-643b192b5/)")

st.markdown("""
<div style='text-align: center; margin-top: 30px; font-size: 15px; color: grey;'>
    Made with ❤️ by Laiba Naz to help you grow every day.
</div>
""", unsafe_allow_html=True)
st.markdown("---")
