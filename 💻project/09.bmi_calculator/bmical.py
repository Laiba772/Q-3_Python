# # BMI CALCULATOR.

# # This is a simple BMI calculator that takes weight and height as input and calculates the BMI. 
# # It also provides feedback on the BMI category.
# # The code is written in Python and uses the Streamlit library for the web interface.
# # The code is multilingual, supporting both English and Urdu languages.


import streamlit as st
import time

# Set config
st.set_page_config(page_title="BMI CALCULATOR", page_icon="😎", layout="centered")

# Language Toggle
lang = st.radio("Select Language / زبان منتخب کریں:", ["English", "اردو"], horizontal=True)

# Multilingual Texts
texts = {
    "English": {
        "title": "Project 9: BMI Calculator In Python",
        "description": "Enter your **weight** and **height** below to find out your BMI!",
        "weight": "Weight (kg):",
        "height": "Height (m):",
        "calculating": "Calculating your BMI...",
        "your_bmi": "📊 Your BMI is:",
        "underweight": "⚠️ You are underweight.",
        "normal": "✅ You have a normal weight. Keep it up!",
        "overweight": "😬 You are overweight.",
        "obese": "🚨 You are obese.",
        "invalid": "Please enter valid weight and height values."
    },
    "اردو": {
        "title": "پروجیکٹ 9: باڈی ماس انڈیکس کیلکولیٹر",
        "description": "نیچے اپنا **وزن** اور **قد** درج کریں اور اپنا BMI معلوم کریں!",
        "weight": "وزن (کلوگرام):",
        "height": "قد (میٹر):",
        "calculating": "...آپ کا BMI نکالا جا رہا ہے",
        "your_bmi": "📊 آپ کا BMI ہے:",
        "underweight": "⚠️ آپ کا وزن کم ہے۔",
        "normal": "✅ آپ کا وزن نارمل ہے۔ زبردست!",
        "overweight": "😬 آپ کا وزن زیادہ ہے۔",
        "obese": "🚨 آپ موٹاپے کا شکار ہیں۔",
        "invalid": "براہ کرم درست وزن اور قد درج کریں۔"
    }
}

t = texts[lang]

st.title(t["title"])
st.markdown(f"## {t['description']}")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input(t["weight"], min_value=1.0, format="%.2f")
with col2:
    height = st.number_input(t["height"], min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    with st.spinner(t["calculating"]):
        time.sleep(1)
        bmi = weight / (height**2)

    st.subheader(t["your_bmi"])
    st.markdown(f"<h2 style='color:#4CAF50;'>{bmi:.2f}</h2>", unsafe_allow_html=True)

    if bmi < 18.5:
         st.error(t["underweight"])
    elif bmi <= 24.9:
        st.success(t["normal"])
    elif bmi <= 29.9:
        st.warning(t["overweight"])
    else:
        st.error(t["obese"])
else:
    st.info(t["invalid"])
