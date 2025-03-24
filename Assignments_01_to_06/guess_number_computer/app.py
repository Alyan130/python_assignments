import random


print("Welcome to Number Guessing game , you have 5 choices to play!")
print("Guess the number between 1-50")

def computer_input():
     number=random.randint(1,50)
     return number

score=0
for count in range(5):
      user_input=int(input("Enter number :"))
      if user_input==computer_input():
         score+=1
         print("correct guess you gain 1 point!")
      else:
         print("wrong guess!")
  

print(f"Your score is : {score}")