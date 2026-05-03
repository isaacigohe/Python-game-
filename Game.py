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
    