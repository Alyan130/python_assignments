import random

die_sides:int=6

def roll_dice():
  die1:int = random.randint(1,die_sides)
  die2:int = random.randint(1,die_sides)
  
  print(f"""
   Die1 : {die1}
   Die2 : {die2}
       """)


def main():
   print("Result of two dices rolled thrice :")
   roll_dice()
   roll_dice()
   roll_dice()
  

if __name__ == '__main__':
    main()