import random

userInput = input("Enter the value,'rock','paper','scissor':")
computerInput = ["rock","paper","scissor"]
print(userInput)
computerValue = random.choice(computerInput)
print(computerValue)

if(userInput == computerValue):
    print("Both Value are same,It's tie")
elif(userInput == "rock"):
    if(computerValue == "scissor"):
        print("rock smashes scissor,you win!")
    else:
        print("paper cover rock, you lose!")
elif(userInput == "paper"):
    if(computerValue == "rock"):
        print("paper cover rock, you win!")
    else:
        print("scissor cut paper, you lose!")
elif(userInput == "scissor"):
    if(computerValue == "paper"):
        print("scissor cut paper, you win!")
    else:
        print("rock smashes scissor, you lose")


