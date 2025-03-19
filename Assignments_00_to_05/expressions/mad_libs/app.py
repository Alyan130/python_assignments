Sentence:str="Code in Place is fun. I learned to program and used Python to make my "

def main():
    adjective: str = input("Please an adjective : ")
    noun: str = input("Please enter a noun : ")
    verb: str = input("Please  enter a verb :  ")

    print(Sentence+adjective+" "+noun+" "+verb)

if __name__ == '__main__':
    main()