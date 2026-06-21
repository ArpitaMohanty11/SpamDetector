import tkinter as tk
from tkinter import messagebox

def check_spam():
    message = entry.get()

    if "win" in message.lower() or "prize" in message.lower():
        result.config(text="🚨 SPAM", fg="red")
    else:
        result.config(text="✅ NOT SPAM", fg="green")

root = tk.Tk()
root.title("AI Spam Detector")
root.geometry("500x350")
root.resizable(False, False)

label = tk.Label(root, text="Enter Message:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(
       root,
       bg="skyblue",
       fg="black",
       text="Check Spam",
       font=("Arial", 12, "bold"),
       width=15,
       command=check_spam
       )
button.pack(pady=10)

root.configure(bg="lightblue")
title = tk.Label(
            root,
              text="AI Spam Detector",
              font=("Arial", 18, "bold"),
              bg="lightblue",
              fg="darkblue"
            )
title.pack(pady=10)


result = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
result.pack()
footer = tk.Label(
    root,
    text="Created by Arpita Mohanty",
    bg="lightblue",
    font=("Arial", 8)
)
footer.pack(side="bottom", pady=5)


root.mainloop()
