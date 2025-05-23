import streamlit as st
import pandas as pd
import random

# Set the title of the app
st.set_page_config(page_title="Student Data Generator", page_icon="🎓", layout="wide")
st.title("🎓 Student CSV File Generator")

# Predefined names
names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah",
         "Bilal", "Ali", "Sara", "Aisha", "Omar", "Fatima", "Zain", "Laila", "Yusuf", "Mariam"]

# Generate student data
students = []
for i in range(1, 21):  # 20 students
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Major": random.choice(["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"]),
        "GPA": round(random.uniform(2.0, 4.0), 2)
    }
    students.append(student)

df = pd.DataFrame(students)

# Show data
st.subheader("📋 Generated Student Data")
st.dataframe(df)

# Download button for CSV file
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download CSV", csv_file, "students.csv", "text/csv", key="download-csv")
st.success("✅ CSV file generated successfully!")

# Add a footer to the app
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Created by :  <span style='color: #ff4b4b;'>Laiba Naz ❤❤</span></h5>",
            unsafe_allow_html=True)
