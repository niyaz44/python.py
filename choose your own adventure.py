name = input("Enter your name:")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You came to a river, you can walk around it or swim, which one would you like to do? ")
    if answer == "swim":
        print("You swim across and were eaten by an crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water amd you lost the game")
    else:
        print("Invalid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, bridge looks slippery, do you want to cross it or head back? ").lower()
    if answer == "head back":
        print("You go back and lose.")
    elif answer == "cross":
        answer == input("You crossed the bridge and meet a strange. Do you want to talk to them (yes/no)? ")


        if answer == "yes":
            print("You talk to a stranger and he gave you 1 million cash. ") 
        elif answer == "no":
            print("You didn't talk to the stranger and you lost 1 million in cash. ")
        else:
            print("Invalid option, You lost")
    else:
        print("Invalid option. You lose.")
   

else:
    print("Invalid option. You lose.")

print("Thank you for trying",name)