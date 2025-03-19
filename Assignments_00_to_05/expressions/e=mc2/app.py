
C: int = 299792458

def main():
  mass:float= float(input("Enter kilos of mass: "))

  energy:float = mass*(C**2) 
  
  print(f"""
    e = m * C^2...
    Mass (m) = {mass}kg
    Speed of light (C) = {C}m/s
    Energy (e) = {energy}Joules
        """)

if __name__ == '__main__':
    main()