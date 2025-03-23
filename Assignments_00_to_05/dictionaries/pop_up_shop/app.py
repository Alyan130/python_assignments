def main():
  fruits = {'apple': 10, 'banana': 20, 'jackfruit': 80, 'kiwi': 5, 'orange': 8, 'mango': 5}    
 
  total_cost=0

  for fruit in fruits:
    price=fruits[fruit]
    fruits_quantity=int(input(f"How many {fruit} do you want to buy?: "))
    total_cost+=(price*fruits_quantity)

  print(f'Your total is ${total_cost}')

if __name__ == '__main__':
    main()