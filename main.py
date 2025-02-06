import tkinter as tk
from number_guessing_game import NumberGuessingGame
from spin_the_wheel import SpinTheWheel
from ui_components import create_label, create_button, clear_window

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Hub")
        self.root.geometry("500x400")
        self.root.configure(bg="lightblue")
        self.root.resizable(False, False)
        self.show_home_screen()

    def show_home_screen(self):
        clear_window(self.root)
        create_label(self.root, "Welcome!", 16, "bold", pady=20, fg="darkblue")

        # Use padx and pady for better spacing
        create_button(self.root, "Play Number Guessing Game", self.start_number_game, 
                      bg="skyblue", fg="darkblue", pady=10, padx=20)  # Added padding
        create_button(self.root, "Play Spin the Wheel Game", self.start_spin_game, 
                      bg="skyblue", fg="darkblue", pady=10, padx=20)  # Added padding


    def start_number_game(self):
        NumberGuessingGame(self.root, self.show_home_screen)

    def start_spin_game(self):
        SpinTheWheel(self.root, self.show_home_screen)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
