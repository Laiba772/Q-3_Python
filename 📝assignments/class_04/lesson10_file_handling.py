# File handling methods with real world examples

# 1. Creating and writing to a file - Example: Saving user registration data
with open("user_data.txt", "w") as file:
    file.write("Name: John Doe\n")
    file.write("Email: john@example.com\n")
    file.write("Age: 25\n")








# 2. Reading from a file - Example: Loading a configuration file
with open("config.txt", "r") as file:
    settings = file.read()






# 3. Appending to a file - Example: Adding transaction logs
with open("transactions.log", "a") as file:
    file.write("2024-01-20: Payment received - $100\n")






# 4. Reading lines - Example: Processing customer orders
with open("orders.txt", "r") as file:
    orders = file.readlines()
    for order in orders:
        print(f"Processing order: {order.strip()}")








# 5. Binary file handling - Example: Saving image file
with open("profile.jpg", "rb") as source:
    with open("profile_backup.jpg", "wb") as target:
        target.write(source.read())







# 6. Checking if file exists - Example: Validating log files
import os
if os.path.exists("system.log"):
    print("Log file found")
else:
    print("Log file not found")








# 7. Creating directories - Example: Organizing project files
if not os.path.exists("project_docs"):
    os.makedirs("project_docs")







# 8. File information - Example: File management system
file_stats = os.stat("data.txt")
print(f"File size: {file_stats.st_size} bytes")
print(f"Last modified: {file_stats.st_mtime}")








# 9. CSV file handling - Example: Processing sales data
import csv
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Quantity", "Price"])
    writer.writerow(["Laptop", 5, 1000])








# 10. JSON file handling - Example: Storing app settings
import json
settings = {
    "theme": "dark",
    "notifications": True,
    "language": "en"
}
with open("settings.json", "w") as file:
    json.dump(settings, file)


