# app/people/customer.py

class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: any) -> None:
        print(f'{self.name} is watching "{movie}".')
