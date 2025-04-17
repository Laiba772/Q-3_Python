# 🪨📄✂️ Project 04: Rock, Paper, Scissors Game in Python

This is a classic **Rock, Paper, Scissors** game built using **Python** where the user plays against the computer.

---

## 🎯 Objective

Create an interactive game where:
- The player chooses between Rock, Paper, or Scissors.
- The computer randomly picks one of the three.
- The winner is decided based on traditional rules.

---

## 🕹️ How to Play

1. Run the game script in your terminal or Python IDE.
2. Enter your choice when prompted: `rock`, `paper`, or `scissors`.
3. The computer will also choose randomly.
4. The winner will be displayed based on the rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice = Tie

---

## 🧠 Game Logic

```python
if player == computer:
    print("It's a tie!")
elif (player == 'rock' and computer == 'scissors') or \
     (player == 'scissors' and computer == 'paper') or \
     (player == 'paper' and computer == 'rock'):
    print("Player wins!")
else:
    print("Computer wins!")

---
## 💻 How to Run the Program

1. Make sure you have **Python** installed on your system.
2. Save the code in a file named `rock_paper_scissors.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder where your file is saved.
5. Run the script using the following command:

```bash
python rock_paper_scissors.py
```
