import random

user_win = 0
computer_win = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Enter Rock/Paper/Scissors or q to quit the game: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("Computer Picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_win += 1
    else:
        print("You lost")
        computer_win += 1

print("You won", user_win,"times.")
print("The computer won", computer_win,"times.")
print("Goodbye! ")