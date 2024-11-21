import random
#intialize the function
def diceroll():
    print("Welcome to Diceroll.")
    startroll = (input("Type roll to roll the dice:"))
    score = 0
    dice = random.randint(1,6)
    if startroll == "roll":
        print(dice)
    coinflip = (input("Type flip to flip the coin"))
    values = ["heads", "tails"]
    if coinflip == "flip":
        coin = random.choice(values)
        print(coin)
    if coin == "heads":
        score = score + dice
    elif coin == "tails":
        score = score - dice
    print("Your score is:", score)
#call function
diceroll()