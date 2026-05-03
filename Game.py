import random

def choose_difficulty():
    """Let player choose difficulty level"""
    print("\nSelect Difficulty Level:")
    print("1. Easy (10 tries)")
    print("2. Medium (7 tries)")
    print("3. Hard (5 tries)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 10, "Easy"
        elif choice == '2':
            return 7, "Medium"
        elif choice == '3':
            return 5, "Hard"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def get_hint(number):
    """Generate a simple hint"""
    if number % 2 == 0:
        return "Hint: The number is even"
    else:
        return "Hint: The number is odd"

def save_score(name, attempts, difficulty):
    """Save score to a text file"""
    with open("scores.txt", "a") as file:
        file.write(f"{name},{attempts},{difficulty}\n")
    print("Score saved!")

def play_game():
    """Main game function"""
    print("=" * 50)
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 50)
    
    # Setup
    max_attempts, difficulty = choose_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0
    wrong_guesses = 0
    
    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    # Game loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            # Validate range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            # Check guess
            if guess == secret_number:
                print(f"\n🎉 Correct! You guessed {secret_number}!")
                print(f"You won in {attempts} attempt(s)!")
                
                # Save high score
                name = input("\nEnter your name: ")
                save_score(name, attempts, difficulty)
                return
            
            elif guess < secret_number:
                print("Too Low!")
                wrong_guesses += 1
            else:
                print("Too High!")
                wrong_guesses += 1
            
            # Give hint after 3 wrong tries
            if wrong_guesses == 3:
                print(get_hint(secret_number))
            
            print(f"Remaining attempts: {max_attempts - attempts}\n")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Game over
    print(f"\n Game Over! The number was {secret_number}")
    print("Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()