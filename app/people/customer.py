# app/people/customer.py
class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name: str = name
        self.food: str = food

    def watch_movie(self, movie_name: str) -> None:
        print(f'{self.name} is watching "{movie_name}".')


