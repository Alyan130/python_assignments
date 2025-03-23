affirmation="I am capable, strong, and ready to achieve my goals"


def main():
    print("Please type the following affirmation: " + affirmation)

    user_input=input("Enter affirmation: ")
    while user_input != affirmation:
       print("That was not the affirmation.")

       print("Please type the following affirmation: " + affirmation)
       user_input=input("Enter affirmation : ")
     
    print("That's right! :)")
        


if __name__ == '__main__':
    main()