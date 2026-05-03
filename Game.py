import random
import os

# File to store high scores
HIGHSCORE_FILE = "highscores.txt"

def display_welcome():
    """Display welcome message and game rules"""
    print("=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    print("\nHow to play:")
    print("- I'll think of a number between 1 and 100")
    print("- You try to guess it!")
    print("- I'll tell you if you're too high or too low")
    print("- Guess correctly to win!\n")

def choose_difficulty():
    """Let user choose difficulty level and return max attempts"""
    print("Choose your difficulty level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    
    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            print("\n✅ Easy mode selected - You have 10 tries!")
            return 10, "Easy"
        elif choice == "2":
            print("\n✅ Medium mode selected - You have 7 tries!")
            return 7, "Medium"
        elif choice == "3":
            print("\n✅ Hard mode selected - You have 5 tries!")
            return 5, "Hard"
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def get_hint(number):
    """Generate a helpful hint about the number"""
    hints = []
    
    if number % 2 == 0:
        hints.append(f"The number is even")
    else:
        hints.append(f"The number is odd")
    
    if number % 5 == 0:
        hints.append(f"divisible by 5")
    elif number % 3 == 0:
        hints.append(f"divisible by 3")
    
    if number > 50:
        hints.append(f"greater than 50")
    else:
        hints.append(f"50 or less")
    
    return f"💡 Hint: {' and '.join(hints)}"

def save_highscore(username, attempts, difficulty):
    """Save the player's score to a file"""
    with open(HIGHSCORE_FILE, "a") as file:
        file.write(f"{username},{attempts},{difficulty}\n")
    print(f"\n🏆 Score saved to leaderboard!")

def display_leaderboard():
    """Display the top scores from the highscore file"""
    if not os.path.exists(HIGHSCORE_FILE):
        print("\n📊 No scores yet! Be the first to play!")
        return
    
    print("\n" + "=" * 50)
    print("🏆 LEADERBOARD (Fewest Attempts Wins!) 🏆")
    print("=" * 50)
    
    # Read all scores
    scores = []
    with open(HIGHSCORE_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                username, attempts, difficulty = parts
                scores.append((username, int(attempts), difficulty))
    
    # Sort by attempts (lowest first)
    scores.sort(key=lambda x: x[1])
    
    # Display top 10
    print(f"{'Rank':<6} {'Player':<15} {'Attempts':<10} {'Difficulty'}")
    print("-" * 50)
    for i, (username, attempts, difficulty) in enumerate(scores[:10], 1):
        print(f"{i:<6} {username:<15} {attempts:<10} {difficulty}")
    print("=" * 50)

def play_game():
    """Main game logic"""
    # Generate random number
    secret_number = random.randint(1, 100)
    
    # Choose difficulty
    max_attempts, difficulty = choose_difficulty()
    attempts = 0
    wrong_guesses = 0
    hint_given = False
    
    print(f"\n🎯 I'm thinking of a number between 1 and 100...")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        # Get user input
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input
            continue
        
        # Check if guess is in valid range
        if guess < 1 or guess > 100:
            print("❌ Please guess a number between 1 and 100!")
            attempts -= 1
            continue
        
        # Check the guess
        if guess == secret_number:
            print(f"\n🎉 CONGRATULATIONS! You guessed it! 🎉")
            print(f"The number was {secret_number}")
            print(f"You won in {attempts} attempt(s)!")
            
            # Save high score
            username = input("\nEnter your name for the leaderboard: ").strip()
            if username:
                save_highscore(username, attempts, difficulty)
            return True
        
        elif guess < secret_number:
            print(f"📈 Too Low!")
            wrong_guesses += 1
        else:
            print(f"📉 Too High!")
            wrong_guesses += 1
        
        # Show remaining attempts
        if remaining > 0:
            print(f"   Remaining attempts: {remaining}\n")
        
        # Give hint after 3 wrong tries
        if wrong_guesses == 3 and not hint_given:
            print(get_hint(secret_number))
            hint_given = True
            print()
    
    # Game over - ran out of attempts
    print(f"\n💔 Game Over! You ran out of attempts.")
    print(f"The number was {secret_number}")
    print("Better luck next time!\n")
    return False

def main():
    """Main program loop"""
    display_welcome()
    
    while True:
        # Show menu
        print("\nMain Menu:")
        print("1. Play Game")
        print("2. View Leaderboard")
        print("3. Exit")
        
        choice = input("\nWhat would you like to do? (1-3): ").strip()
        
        if choice == "1":
            play_game()
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()