
def get_user_input()->list[int]:
   user_numbers:list[int]=[]
    
   while True:
      number_input:int= int(input("Enter number : "))
      user_numbers.append(number_input)
   
      add_more:str= input("Enter more (y/n): ")
      if add_more.lower()=="y":
         pass
      else:
         break
      
   return user_numbers

def main():
    num_dict={}
    for num in get_user_input():
       if num not in num_dict:
          num_dict[num]=1
       else:
          num_dict[num]+=1
     
    for key,value in num_dict.items():
      print(f"{key} appears {value} times.")

if __name__ == '__main__':
    main()