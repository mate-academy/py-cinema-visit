class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: list) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for cust in customers:
            if type(cust) != dict:
                print(f'{cust.name} is watching "{movie_name}".')
            else:
                print(f'{cust["name"]} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        if type(cleaning_staff) == str:
            print(f"Cleaner {cleaning_staff} is cleaning "
                  f"hall number {self.number}.")
        else:
            print(f"Cleaner {cleaning_staff.name} is "
                  f"cleaning hall number {self.number}.")
