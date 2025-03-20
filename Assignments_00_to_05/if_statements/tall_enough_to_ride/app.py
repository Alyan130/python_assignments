minimum_height=40

def main():
  user_permission = True
  while user_permission:
     height:str = (input("How tall are you? "))
      
     if height.lower()=="stop":
        user_permission=False
     else:
         if int(height) > 40 :
           print("You're tall enough to ride!")
         else:
           print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()