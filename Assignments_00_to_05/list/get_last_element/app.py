def get_last_element(lst):
    print(lst[-1])


def get_list():
    my_list=[]
   
    user_input=input("Enter number : ")
    while user_input!="":
     my_list.append(user_input)
     user_input=input("Enter number : ")
     
    return my_list


def main():
  lst= get_list()
  get_last_element(lst)


if __name__ == '__main__':
    main()