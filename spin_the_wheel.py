import random
import tkinter as tk
from tkinter import messagebox
from ui_components import create_label, create_button, create_entry, clear_window

class SpinTheWheel:
    def __init__(self, root, go_back_callback):
        self.root = root
        self.go_back_callback = go_back_callback
        self.previous_spin = random.randint(1, 100)
        self.streak = 0

    def play_spin_wheel(self):
        """Starts the spin-the-wheel game."""
        clear_window(self.root)
        create_label(self.root, f"Spun Number: {self.previous_spin}", 14, pady=20)
        create_button(self.root, "Spin the Wheel!", self.spin_wheel)
        create_label(self.root, "Will the next number be higher or lower?", 12, pady=10)
        self.guess_entry = create_entry(self.root)
        create_button(self.root, "Submit Guess", self.check_guess, pady=10)
        self.feedback_label = create_label(self.root, "", 12, fg="blue", pady=10)
        self.streak_label = create_label(self.root, f"Streak: {self.streak}", 12, fg="purple", pady=10)
        create_button(self.root, "Back to Home", self.go_back_callback, pady=10)

    def spin_wheel(self):
        """Generates a new spin and updates the UI."""
        self.previous_spin = random.randint(1, 100)
        self.play_spin_wheel()

    def check_guess(self):
        """Checks the user's guess."""
        guess = self.guess_entry.get().lower()
        new_spin = random.randint(1, 100)

        if guess not in ["higher", "lower"]:
            self.feedback_label.config(text="Please guess 'higher' or 'lower'.", fg="red")
            return

        if (guess == "higher" and new_spin > self.previous_spin) or (guess == "lower" and new_spin < self.previous_spin):
            self.streak += 1
            self.feedback_label.config(text=f"Correct! Streak: {self.streak}", fg="green")
        else:
            self.streak = 0
            self.feedback_label.config(text=f"Incorrect! Streak reset. New number was {new_spin}.", fg="red")

        self.previous_spin = new_spin
        self.streak_label.config(text=f"Streak: {self.streak}")
