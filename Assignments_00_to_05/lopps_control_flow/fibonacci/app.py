max_term : int = 10000

def main():
    curr_term = 0 
    next_term = 1 
    while curr_term <= max_term:
        print(curr_term)
        calculated_term=curr_term+next_term
        curr_term=next_term
        next_term=calculated_term
     


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()