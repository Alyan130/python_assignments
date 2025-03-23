def read_phone_number():
  phonebook={}
   
  while True:
    name=input("Enter name : ")
    if name=="":
       break
    number=int(input("Enter number: "))
    phonebook[name]=number
    
  return phonebook


def print_phonebook(phonebook):
   for name,number in phonebook.items():
      print(f"{name} ---> {number}")

def find_number(phonebook):
   while True:
       search_name =input("Enter name to lookup :") 

       if search_name==" ":
         break
       
       if search_name in phonebook:
           print(f"{search_name} ---> {phonebook[search_name]}")
       else:
          print(f"{search_name} not found!")
       
    

def main():   
  phonebook = read_phone_number()
  print_phonebook(phonebook)
  find_number(phonebook)


if __name__ == '__main__':
    main()