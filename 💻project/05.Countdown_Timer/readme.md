# ⏳ Project 05: Countdown Timer in Python

This is a simple and interactive **Countdown Timer** built using Python. It allows the user to enter time in seconds, and then displays a real-time countdown on the screen in **MM:SS** format.

---

## 🎯 Objective

The goal of this project is to:

- Accept user input for countdown time in seconds.
- Display the countdown in a clean and readable **minutes:seconds (MM:SS)** format.
- Update the timer in real time on the same line.
- Show a final message when the time is up.

---

## 💡 How It Works

1. The program asks the user to enter time (in seconds).
2. The input is validated to make sure it's a **positive integer**.
3. The countdown starts and keeps updating every second.
4. Once the countdown reaches 0, it prints:


## 🧾 Code Summary

- `random` module is **not used**.
- `time.sleep(1)` is used to wait for 1 second between updates.
- `divmod(seconds, 60)` splits total seconds into minutes and seconds.
- `try-except` block ensures that invalid inputs (like letters) are handled gracefully.
- The loop continues until the timer reaches zero.

---

## 💻 How to Run the Program

### ✅ Requirements

- Python 3.x
- No external libraries required

### 🧪 Steps to Run:

1. Save the Python code in a file named: `countdown_timer.py`
2. Open **Command Prompt**, **Terminal**, or any code editor terminal.
3. Navigate to the directory where your file is saved.
4. Run the following command:

```bash
python count.py
