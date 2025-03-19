from math import sqrt

def main():
   AB:float = float(input("Enter the length of AB: "))
   AC:float = float(input("Enter the length of AC: "))

   BC = sqrt((AB**2) + (AC**2))  
   print(f"The length of BC (the hypotenuse) is: {BC}")

if __name__ == '__main__':
    main()  