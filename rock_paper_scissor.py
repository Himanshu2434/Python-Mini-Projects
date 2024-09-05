"""
Workflow Of Project :
1- Input from user (rock , paper , scissor )
2- Computer choice (Computer will choose randomly not conditionally)
3- Compare user choice and computer choice
4- Display result (win , lose , tie)

case 1 :

rock - rock = tie
rock - paper = lose
rock - scissor = win

case 2 :
paper - rock = win
paper - paper = tie
paper - scissor = lose

case 3 :
scissor - rock = lose
scissor - paper = win
scissor - scissor = tie

"""
import random

print("---------------------Welcome-----------------------------\n")

# Get user choice
# convert user input to lower case to make it case insensitive
user_choice = input("Enter your choice(rock,paper,scissor) : ").lower()

# computer will choose randomly from rock , paper , scissor
computer_choice = random.choice(["rock","paper","scissor"])

# display user choice and computer choice
print(f"\nYour Choice :",user_choice)
print(f"\nComputer Choice : ",computer_choice)

#display result
print("\nResult : ")
if user_choice == computer_choice:
    print("tie")
elif user_choice == "rock" and computer_choice == "scissor":
    print("You win")
elif user_choice == "scissor" and computer_choice == "rock":
    print("You lose")
elif user_choice == "paper" and computer_choice == "scissor":
    print("You lose")
elif user_choice == "scissor" and computer_choice == "paper":
    print("You win")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win")
else :
    print("Invalid input")