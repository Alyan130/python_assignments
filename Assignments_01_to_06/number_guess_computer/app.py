import random
import time

def computer_guess(low, high):
    while low <= high:
        guess = random.randint(low, high)
        print(f"Computer guesses: {guess}")
        user_input = input("Type 'too high', 'too low', or 'correct': ").lower()

        if user_input == "too high":
            high = guess - 1
        elif user_input == "too low":
            low = guess + 1
        elif user_input == "correct":
            print(f"Computer guessed your number: {guess}!")
            break
        else:
            print("Invalid input! Please type 'too high', 'too low', or 'correct'.")

def main():
    print("Think of a number between 1 and 100. The computer will try to guess it.")
    input("Press Enter when you're ready...")
    time.sleep(1)
    print("loading...",end="\r")
    time.sleep(1)
    print("start",end="\r")

    computer_guess(1,5)

main()
