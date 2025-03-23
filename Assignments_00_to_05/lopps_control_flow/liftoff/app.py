start_count:int=10
end_count:int=0

def main():
   for count in range(start_count,end_count,-1):
       print(count,end=" ")
    
   print("liftoff!")


if __name__ == '__main__':
    main()