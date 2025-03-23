
max_lenth=2

def shorten_list(lst):
   while len(lst) != max_lenth: 
       removed_elem =  lst.pop()
       print(removed_elem,end=" ")


def get_lst():
    lst = []
    element = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        lst.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
  lst= get_lst()
  shorten_list(lst)


if __name__ == '__main__':
    main()