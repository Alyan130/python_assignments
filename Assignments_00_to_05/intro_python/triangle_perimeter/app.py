def main():
   side_one:float = float(input("What is the length of side 1? "))
   side_two:float = float(input("What is the length of side 2? "))
   side_three:float = float(input("What is the length of side 3? "))
   
   Perimeter:float =  side_two+side_two+side_three

   print(f"The perimeter of the triangle is {Perimeter}") 

if __name__ == '__main__':
    main()