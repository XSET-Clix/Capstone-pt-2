import random

# Define the game logic
def play_game(uc, rc):
    if uc == rc:
        print(f"Both chose {uc}. It's a Tie!")
    elif (uc == "rock" and rc == "scissors") or \
         (uc == "paper" and rc == "rock") or \
         (uc == "scissors" and rc == "paper"):
        print(f"You chose {uc} and the computer chose {rc}. You win!")
    else:
        print(f"You chose {uc} and the computer chose {rc}. You lose!")

# Main game loop
def game():
    print("Welcome to the Rock, Paper, Scissors Game.")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Play the round
        play_game(user_choice, computer_choice)

        # Ask to continue or exit
        option = input("Do you want to play again? (yes/no): ").lower()
        if option != "yes":
            print("Thank you for playing!")
            break

# Start the game
if __name__ == "__main__":
    game()


