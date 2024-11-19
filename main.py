import random
cc = ["rock", "paper", "scissors"]
rc = random.choice(cc)
#rock
def rock(uc):
    if rc == "rock":
        if uc == "rock":
            print("Tie")
        elif uc == "paper":
            print("You win!")
        elif uc == "scissors":
            print("You lose")
        else:
            print("Invalid Option")
#paper
def paper(uc):
    if rc == "paper":
        if uc == "paper":
            print("Tie")
        elif uc == "scissors":
            print("You win!")
        elif uc == "rock":
            print("You lose")
        else:
            print("Invalid Option")
#scissors            
def scissors(uc):
    if rc == "scissors":
        if uc == "scissors":
            print("Tie")
        elif uc == "rock":
            print("You win!")
        elif uc == "paper":
            print("You lose")
        else:
            print("Invalid Option")
#while loop
def game():
    choice = input("Enter Your Choice:")
    while True:
        if choice.lower() == "rock":
            rock(choice)
        elif choice.lower() == "paper":
            paper(choice)
        elif choice.lower() == "scissor":
            scissors(choice)
        else:
            print("Invaild Option")
        print("Do you wanna continue?")
        option = input("yes/no")
        if option.lower() == "yes":
            game()
        else:
            print("Thank you playing")
            break
        


if __name__ == "__main__":
    print("Welcome to the Rock, Paper, and, Scissor Game.")
    game()