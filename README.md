# Random Number Guessing

Overview
Random Number Guessing is a Python-based GUI application that brings together multiple mini-games in one place. Built using Tkinter, it currently features:
• Number Guessing Game: Guess the randomly generated number within a specified range.
• Spin the Wheel: Predict whether the next spun number will be higher or lower.
This interactive game collection provides a fun and engaging experience while demonstrating Python's GUI capabilities.

--------------------------------------------------

## Features

Number Guessing Game
• Customizable Range: Users set a minimum and maximum number for the guessing range.
• Real-Time Feedback: Hints help guide players toward the correct number.
• Limited Attempts: Players have a set number of attempts to guess correctly.
• Restart and Home Options: Players can restart or return to the home screen at any time.
• Dynamic Difficulty Adjustment: The game dynamically sets the number of allowed attempts based on the selected range.

Spin the Wheel
• Random Number Generation: Each spin produces a new random number between 1 and 100.
• Higher or Lower Guessing: Players predict if the next spin will be higher or lower than the previous number.
• Streak Counter: Tracks the player's consecutive correct guesses.
• User-Friendly Interface: Clear labels and buttons enhance usability.
• Instant Feedback: Displays results and updates streak count in real-time.

--------------------------------------------------

## How to Play

Number Guessing Game
1. Select the "Play Number Guessing Game" option on the home screen.
2. Enter a minimum and maximum number to define the guessing range.
3. Enter your guess and click "Check."
4. Receive feedback and keep guessing until you succeed or run out of attempts.
5. Restart or return to the home screen at any time.

Spin the Wheel
1. Select the "Play Spin the Wheel Game" option on the home screen.
2. View the current spun number.
3. Predict if the next number will be higher or lower.
4. Enter "higher" or "lower" and submit your guess.
5. Try to build the longest correct streak!
6. Restart or return to the home screen at any time.

--------------------------------------------------

### Requirements
• Python 3.x
• Tkinter (bundled with Python)

--------------------------------------------------

### Installation and Running the Game

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository:
   git clone https://github.com/dimple2001/number-guessing-game
   cd number-guessing-game
3. Run the game:
   python main.py

--------------------------------------------------

### Project Structure
number-guessing-game/
│-- main.py               # Main application file
│-- number_guessing_game.py  # Number Guessing Game logic
│-- spin_the_wheel.py        # Spin the Wheel Game logic
│-- ui_components.py         # UI helper functions
│-- README.md                # Project documentation

--------------------------------------------------

### How It Works

Core Functionalities
• Main: Handles the main menu and game navigation.
• NumberGuessingGame: Manages number input, feedback, and attempts.
• SpinTheWheel: Controls spin generation, guessing, and streak tracking.
• ui_components: Provides reusable UI elements like buttons, labels, and entry fields.
