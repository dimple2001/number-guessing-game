import random
import tkinter as tk
from tkinter import messagebox
from ui_components import create_label, create_button, create_entry, clear_window

class NumberGuessingGame:
    def __init__(self, root, go_back_callback):
        self.root = root
        self.go_back_callback = go_back_callback
        self.best_score = None  # Not used in current version, but could be added later
        self.min_number = None
        self.max_number = None
        self.attempts = 0
        self.max_attempts = 0
        self.get_user_range() # Start by getting the range immediately

    def get_user_range(self):
        """Ask user for custom range."""
        clear_window(self.root)
        self.root.configure(bg="lightgray") # Added background color
        create_label(self.root, "Enter the number range:", 14, pady=10, fg="darkblue") # Added color
        create_label(self.root, "Min:", 12, fg="blue") # Added color
        self.min_entry = create_entry(self.root)
        create_label(self.root, "Max:", 12, fg="blue") # Added color
        self.max_entry = create_entry(self.root)
        create_button(self.root, "Start Game", self.start_game, bg="green", fg="white") # Added colors

    def start_game(self):
        """Starts the game with user-defined range."""
        try:
            self.min_number = int(self.min_entry.get())
            self.max_number = int(self.max_entry.get())

            if self.min_number >= self.max_number:
                messagebox.showerror("Error", "Minimum must be less than maximum.")
                return

            self.target_number = random.randint(self.min_number, self.max_number)
            self.attempts = 0
            self.max_attempts = max(5, (self.max_number - self.min_number) // 4)

            self.game_screen()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def game_screen(self):
        """Displays the game screen."""
        clear_window(self.root)
        self.root.configure(bg="lightgreen")  # Added background color
        create_label(self.root, f"Guess a number between {self.min_number} and {self.max_number}", 14, pady=20, fg="darkgreen")  # Added color
        self.entry = create_entry(self.root)
        create_button(self.root, "Check", self.check_guess, bg="green", fg="white")  # Added colors
        self.feedback_label = create_label(self.root, "", 12, fg="blue", pady=10)
        self.attempt_label = create_label(self.root, f"Attempts: {self.attempts}/{self.max_attempts}", 12, fg="purple", pady=10)
        create_button(self.root, "Restart", self.get_user_range, pady=10, bg="yellow", fg="brown")  # Added colors
        create_button(self.root, "Back to Home", self.go_back_callback, pady=10, bg="orange", fg="white")  # Added colors

    def check_guess(self):
        """Checks the user's guess."""
        try:
            guess = int(self.entry.get())

            if guess < self.min_number or guess > self.max_number:
                self.feedback_label.config(text=f"Enter a number between {self.min_number} and {self.max_number}.", fg="red")
                return

            self.attempts += 1
            self.attempt_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"You've used all attempts! The number was {self.target_number}.")
                self.get_user_range()  # Go back to range selection
                return

            difference = abs(guess - self.target_number)

            if guess == self.target_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.get_user_range()  # Go back to range selection
            elif difference <= 5:
                self.feedback_label.config(text="Very Close! Try again.", fg="orange")
            elif difference <= 10:
                self.feedback_label.config(text="Close, but a bit off. Try again.", fg="blue")
            elif guess < self.target_number:
                self.feedback_label.config(text="Too Low! Try a higher number.", fg="blue")
            else:
                self.feedback_label.config(text="Too High! Try a lower number.", fg="blue")

        except ValueError:
            self.feedback_label.config(text="Invalid input. Enter a number.", fg="red")