print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
        quit()

print("Okay! Lets's play :)")
score=0

answer = input("What does CPU sand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score=score+1
else:
    print("Incorrect!")
answer = input("What does GPU stands for? ")
if answer.lower() == 'graphics processing unit':
     print("Correct")
     score=score+1
else:
     print("Incorrect")
answer = input("What does RAM stands for? ")
if answer.lower() == 'random access memory':
     print("Correct")
     score=score+1
else:
     print("Incorrect")
answer = input("What does PSU stands for? ")
if answer.lower() == 'power supply':
     print("Correct")
     score=score+1
else:
     print("Incorrect")
answer = input("What does IP stands for? ")
if answer.lower() == 'internet protocol':
     print("Correct")
     score=score+1
else:
     print("Incorrect")

print("YOU GOT " + str(score) + " QUESTION CORRECT ")
print("YOU GOT " + str((score/5)*100) + "%.")