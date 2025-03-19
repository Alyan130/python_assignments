
days_in_year: int = 365
hours_in_day: int = 24
min_in_hour: int = 60
sec_in_min: int = 60


def main():
   
    print(f"There are {days_in_year * hours_in_day * min_in_hour * sec_in_min} seconds in a year!")


if __name__ == '__main__':
    main()