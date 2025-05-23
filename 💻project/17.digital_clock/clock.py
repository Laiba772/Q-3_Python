import tkinter as tk
from time import strftime

# Root window
root = tk.Tk()
root.title("DIGITAL CLOCK")
root.resizable(False, False)

# Set fixed window size and center it on the screen
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Title Label
title = tk.Label(root, text="Digital Clock", font=("calibri", 20, "bold"))
title.pack(pady=10)

# Clock Label
label = tk.Label(root, font=("calibri", 40, "bold"), background="yellow", foreground="black")
label.pack(anchor="center", pady=10)

# Time update function
def time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()
