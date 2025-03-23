import random

secret_number=random.randint(1,99)

def main():
   while True:
     guess_number=int(input("Enter number to guess"))
     if secret_number < guess_number:
         print("Too high")
     elif secret_number > guess_number:
        print("Too low")  
     else:
        print("Your guess is correct!")
        break

if __name__ == '__main__':
    main()