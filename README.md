# Number Guessing Game

## Overview

The **Number Guessing Game** is an interactive and fun GUI-based game built with Python's Tkinter library. Players attempt to guess a randomly generated number based on the selected difficulty level, with instant feedback and best score tracking.

## Features

- **Three Difficulty Levels:**
  - Easy (1-50)
  - Medium (1-100)
  - Hard (1-200)
- **User-Friendly Interface:** Simple and intuitive design for all players.
- **Real-Time Feedback:** Instant hints if your guess is too low, too high, or correct.
- **Best Score Tracking:** Records the fewest attempts for each session.
- **Restart Anytime:** Start a new game with one click.

## How to Play

1. **Launch the game**: Run the script to open the game window.
2. **Choose a difficulty**: Select Easy, Medium, or Hard.
3. **Make a guess**: Enter a number and click **Check**.
   - Feedback will guide you:
     - "Too Low!"
     - "Too High!"
     - "Correct!"
4. **Win the game**: See your total attempts and compare it with your best score.
5. **Restart**: Play again by clicking the Restart button.

## Requirements

- Python 3.x
- Tkinter (bundled with Python)

## Installation

1. Ensure Python 3.x is installed.
2. Download or clone this repository.
3. Navigate to the script folder.
4. Run the script:
   ```bash
   python number_guessing_game.py
   ```

## How It Works

The game uses the **`NumberGuessingGame`**** class**, which handles:

- Initializing the game window and variables.
- Displaying start and game screens.
- Tracking attempts and providing feedback.
- Restarting the game while retaining the best score.

### Key Functions

- `create_start_screen`: Displays the welcome screen and difficulty options.
- `start_game`: Sets up the game for the chosen difficulty.
- `create_game_screen`: Shows the main guessing interface.
- `check_guess`: Validates guesses and updates feedback.
- `end_game`: Handles the win state and updates the best score.

## Example Usage

Run the following code to start the game:

```python
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
```

##
