# 🎓 Project 10: Student CSV File Generator

This project creates a Streamlit-based web app that generates random student data and allows you to download it as a CSV file.

---

## 🎯 Objective

- Generate a table of random student data (Name, Age, Major, GPA).
- Display the data in a web-based interface.
- Provide a button to download the data as a CSV file.

---

## ⚙️ Features

- Generates a dataset of 20 random students.
- Each student has:
  - Unique ID
  - Randomly selected Name
  - Age (between 18-25)
  - Random Major (e.g., CS, Math, Physics, etc.)
  - GPA (between 2.0 to 4.0)
- Instant preview in a DataFrame.
- One-click CSV file download.
- Clean and responsive Streamlit UI.

---

## 🧠 How It Works

- Uses Python libraries: `streamlit`, `pandas`, `random`.
- Randomly picks names and values for each student.
- Displays the data in an interactive DataFrame.
- Converts the DataFrame to CSV and provides a download button.

---

## 💻 How to Run the Program

1. Make sure Python is installed on your system.
2. Install the required packages using pip:

```bash
pip install streamlit pandas
```

3.Save the code in a file, for example: student_generator.py.

4.Open a terminal and navigate to the folder where the file is saved.

5.Run the Streamlit app:

```bash

streamlit run student_generator.py

```

6.📁 Output

The generated CSV file will contain 20 students with random details.

File name: students.csv
