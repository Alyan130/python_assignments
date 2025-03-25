import random

def computer_choice():
   options=["rock","paper","scissors"]
   computer_select = random.choice(options)
   return computer_select

def play_game():
    user_input = input("Enter your choice from rock, paper, or scissors: ").lower()
    while user_input:
        computer_select = computer_choice() 
        if user_input == "rock" and computer_select == "scissors" or \
           user_input == "scissors" and computer_select == "paper" or \
           user_input == "paper" and computer_select == "rock":
            print("User won!")
        elif user_input == "scissors" and computer_select == "rock" or \
             user_input == "paper" and computer_select == "scissors" or \
             user_input == "rock" and computer_select == "paper":
            print("Computer won!")
        else:
            print("Tie!")
        
        print(f"Computer chose {computer_select}")
        user_input = input("Enter your choice from rock, paper, or scissors: ").lower()


print("Welcome to ROCK , PAPER and SCISSORS'S game!")
start=input("Press enter to start...")
play_game()


