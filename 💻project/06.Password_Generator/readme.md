# 🔐 Project 06: Password Generator in Python

This project is a **secure and customizable Password Generator** built using Python. It generates strong, random passwords of a user-defined length, ensuring a mix of uppercase, lowercase, digits, and special characters.

---

## 🎯 Objective

To create a Python program that:

- Asks the user for a desired password length.
- Ensures the password contains at least:
  - 1 uppercase letter
  - 1 lowercase letter
  - 1 digit
  - 1 special character
- Randomly fills the remaining characters.
- Outputs a strong and secure password.

---

## 🛡️ Why Use This?

- Helps generate complex passwords that are hard to guess.
- Adds an extra layer of security for your online accounts or projects.
- Fully customizable in length.

---

## 🧪 Example Output


> ✅ Note: The output will be different every time due to randomness.

---

## 💡 Features

- Validates user input.
- Ensures at least one character from each important category.
- Uses Python’s `random` and `string` modules.
- Randomly shuffles characters for better security.

---

## 📋 Code Breakdown

- `string.ascii_uppercase` – A–Z
- `string.ascii_lowercase` – a–z
- `string.digits` – 0–9
- `string.punctuation` – !@#$%^&*()_+... and more

The first four characters are chosen one from each category, then the rest are filled randomly, followed by a shuffle to make it completely unpredictable.

---

## 🔁 Input Validation

- If the entered length is **less than 4**, it asks again (at least 4 characters are required to meet all conditions).
- If a non-integer is entered, it shows an error message.

---

## 💻 How to Run

### ✅ Requirements

- Python 3.x
- No external libraries needed

### 🧪 Steps to Run:

1. Save the script in a file named: `password.py`
2. Open terminal / command prompt.
3. Navigate to the file directory.
4. Run this command:

```bash
python password.py

