  # Lesson 09: Exception Handling

  # 1. Try-Except block - File Reading Example
try:
      file = open("nonexistent_file.txt", "r")
      content = file.read()
      print(content)
except FileNotFoundError:
      print("Error: File does not exist!")




  # 2. Try with else - Age Verification Example

try:
      age = int(input("Enter your age: "))
except ValueError:
      print("Please enter a valid number!")
else:
      if age >= 18:
          print("You are eligible to vote!")
      else:
          print("You are not eligible to vote yet.")




  # 3. Try with finally - Database Connection Example

def simulate_db_connection():
      print("Database connected")
      return "connection_object"

def simulate_db_close(connection):
      print("Database connection closed")

connection = None
try:
      connection = simulate_db_connection()
      # Simulate some database operations
      print("Performing database operations...")
except Exception as e:
      print("Database error occurred:", e)
finally:
      if connection:
          simulate_db_close(connection)





  # 4. Catching multiple exceptions - Calculator Example


try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      result = num1 / num2
      print(f"Result: {result}")
except ValueError:
      print("Please enter valid numbers!")
except ZeroDivisionError:
      print("Cannot divide by zero!")
except Exception as e:
      print("An unexpected error occurred:", e)






  # 5. Raise custom exception - Bank Account Example

  
class InsufficientFundsError(Exception):
      pass

class BankAccount:
      def __init__(self, balance):
          self.balance = balance
    
      def withdraw(self, amount):
          if amount > self.balance:
              raise InsufficientFundsError("Not enough balance in account!")
          self.balance -= amount
          return f"Withdrawn {amount}. New balance: {self.balance}"

try:
      account = BankAccount(1000)
      print(account.withdraw(1500))
except InsufficientFundsError as e:
      print("Transaction failed:", e)
