import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Write Rock/Paper/Scissors or Q to quit:").lower()
    
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #Chooses a number from 0, 1 or 2. resulting in either rock, paper or scissors
    computer_pick = options[random_number]
    print("Computer picked: " + computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1        

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")

    else:
        print("You lost")
        computer_wins += 1

print("User score: ", user_wins)
print("Computer score: ", computer_wins)
print("Goodbye!")

