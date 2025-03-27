PROMPT:str = "What do you want? : "  
JOKE:str = "I'm reading a book about anti-gravity. I can't put it down."
SORRY:str =  "Sorry I only tell jokes."


def main():
   user_input=input(PROMPT).lower() 
   if user_input=="joke":
       print(JOKE)
   else:
       print(SORRY)  
 
if __name__ == '__main__':
    main()