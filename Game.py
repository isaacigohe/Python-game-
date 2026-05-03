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
 