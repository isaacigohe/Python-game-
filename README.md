# Python-game-

# Guess Me

## . Contributor
- **Isaac Igohe**

## . Overview
- Guess Me is a simple, interactive Python console application where the player tries to guess a randomly generated number within a set number of attempts based on the chosen difficulty.
- The game tests logic, estimation, and probability while keeping gameplay fun and engaging. It uses Python's built-in random module for number generation and handles user input robustly with proper error checking.

## . Installation
Follow these steps to set up and run the project locally:

1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/guess-me.git
cd guess-me
```

2. Run the Game
- The project requires Python 3 or later.
```bash
python simple_guess_game.py
```

## . Usage
1. Launch the Game
   - Run the Python file.
   - You'll be prompted to select a difficulty level:
     - 1: Easy → 10 tries
     - 2: Medium → 7 tries
     - 3: Hard → 5 tries

2. Guess the Number
   - Input guesses between 1 and 100.
   - Receive hints if your guess is too high or too low.
   - Game ends when you guess correctly or run out of attempts.

## . Features
1. Interactive Gameplay
   - Console-based interface with real-time feedback on user guesses.
   - Difficulty levels that dynamically adjust the number of attempts.

2. Input Validation
   - Handles invalid inputs and out-of-range guesses gracefully.

3. Randomized Challenge
   - Each session generates a new random number between 1 and 100 for unique playthroughs.

4. Hint System
   - Provides helpful hints after 3 wrong guesses.

5. High Score Tracking
   - Saves player scores to a text file for persistence.

6. Simple and Lightweight
   - No external dependencies beyond Python's standard library.

## . Tech Stack
- Programming Language: Python 3
- Random Number Generation: random module
- File I/O: Built-in file handling
- Execution Environment: Console / Terminal