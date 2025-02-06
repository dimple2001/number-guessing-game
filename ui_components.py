import tkinter as tk

def create_label(root, text, size, weight="normal", pady=0, fg="black", bg=None):
    """Creates and returns a label."""
    label = tk.Label(root, text=text, font=("Arial", size, weight), fg=fg, bg=bg)
    label.pack(pady=pady)
    return label

def create_button(root, text, command, pady=0, padx=0, bg=None, fg=None):  # Added padx
    """Creates and returns a button."""
    button = tk.Button(root, text=text, command=command, bg=bg, fg=fg, padx=padx)  # Added padx to the button
    button.pack(pady=pady)
    return button

def create_entry(root):
    """Creates and returns an entry field."""
    entry = tk.Entry(root)
    entry.pack(pady=10)
    return entry

def clear_window(root):
    """Clears all widgets from the window."""
    for widget in root.winfo_children():
        widget.destroy()