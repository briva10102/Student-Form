import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Notes Subscription")
root.geometry("400x450")
root.configure(bg="#1e1e1e")  # Dark background

# Common styles for dark mode
bg_color = "#1e1e1e"
fg_color = "#f5f5f5"

# Title label
title_label = tk.Label(root, text="📚 Notes Subscription Form", font=("Helvetica", 16, "bold"),
                       bg=bg_color, fg="#00bfff")
title_label.pack(pady=10)

# Name label
label = tk.Label(root, text="Enter your name:", bg=bg_color, fg=fg_color, font=("Arial", 12))
label.pack()

# Entry box
entry = tk.Entry(root, width=25, font=("Arial", 12), bg="#2e2e2e", fg=fg_color,
                 insertbackground=fg_color)
entry.pack(pady=5)

# Checkbuttons
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
check_var3 = tk.BooleanVar()
check_var4 = tk.BooleanVar()

checkbutton1 = tk.Checkbutton(root, text="Chemistry Notes Download", variable=check_var1,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
checkbutton1.pack(anchor="w", padx=20)

checkbutton2 = tk.Checkbutton(root, text="PRS Notes Download", variable=check_var2,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
checkbutton2.pack(anchor="w", padx=20)

checkbutton3 = tk.Checkbutton(root, text="Python Notes Download", variable=check_var3,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
checkbutton3.pack(anchor="w", padx=20)

checkbutton4 = tk.Checkbutton(root, text="EGD Notes Download", variable=check_var4,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
checkbutton4.pack(anchor="w", padx=20)

# Radiobuttons
radio_var = tk.IntVar()

radiobutton1 = tk.Radiobutton(root, text="Download PDF", variable=radio_var, value=1,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
radiobutton1.pack(anchor="w", padx=20)

radiobutton2 = tk.Radiobutton(root, text="Print", variable=radio_var, value=2,
                              bg=bg_color, fg=fg_color, activebackground=bg_color,
                              activeforeground=fg_color, selectcolor=bg_color, font=("Arial", 10))
radiobutton2.pack(anchor="w", padx=20)

# Button actions
def on_button_click():
    selected_notes = []
    if check_var1.get():
        selected_notes.append("Chemistry")
    if check_var2.get():
        selected_notes.append("PRS")
    if check_var3.get():
        selected_notes.append("Python")
    if check_var4.get():
        selected_notes.append("EGD")

    name = entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Please enter your name!")
        return

    if radio_var.get() == 1:
        option = "Download PDF"
    elif radio_var.get() == 2:
        option = "Print"
    else:
        option = "None"

    message = (
        f"Name: {name}\n"
        f"Subscribed to: {', '.join(selected_notes) if selected_notes else 'None'}\n"
        f"Selected Option: {option}"
    )
    messagebox.showinfo("Subscription Details", message)

def reset_form():
    entry.delete(0, tk.END)
    check_var1.set(False)
    check_var2.set(False)
    check_var3.set(False)
    check_var4.set(False)
    radio_var.set(0)

# Buttons
submit_button = tk.Button(root, text="Submit ✅", command=on_button_click,
                          font=("Arial", 12, "bold"),
                          bg="green", fg="white",
                          activebackground="#228B22", activeforeground="white")
submit_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset 🔄", command=reset_form,
                         font=("Arial", 12, "bold"),
                         bg="red", fg="white",
                         activebackground="#8B0000", activeforeground="white")
reset_button.pack(pady=5)

# Run application
root.mainloop()
