def add_numbers(lst:list[int]):
    sum:int=0
    for num in lst:
        sum+=num
    return sum


def main():
    numbers: list[int] = [1, 2, 3, 4, 5] 
    sum_of_numbers: int = add_numbers(numbers) 
    print(sum_of_numbers) 
    

if __name__ == '__main__':
    main()