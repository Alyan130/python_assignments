
def print_list(lst):
   print("Here's the list",end=" ")
   print(lst)


def main():
  my_list=[]
  user_input=input("Enter a value: ")
  while user_input!="":
      my_list.append(user_input)
      user_input=input("Enter a value")

  print_list(my_list)

 
if __name__ == '__main__':
    main()