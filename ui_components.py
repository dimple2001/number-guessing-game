import tkinter as tk
from tkinter import ttk

def create_label(root, text, font_size, font_weight="normal", fg=None, pady=0):
    label = tk.Label(root, text=text, font=("Arial", font_size, font_weight), fg=fg)
    label.pack(pady=pady)
    return label

def create_button(root, text, command, pady=5):
    button = tk.Button(root, text=text, font=("Arial", 12), command=command)
    button.pack(pady=pady)
    return button

def create_entry(root):
    entry = ttk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)
    return entry



