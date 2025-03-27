import random 

Numbers=10
start_range=1
end_range=100

def main():
    i = 1 
    while i <=Numbers:
      number=random.randint(start_range,end_range)
      print(number)     
      i+=1
      
    
if __name__ == '__main__':
    main()