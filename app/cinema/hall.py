class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self):
        print("The hall is being cleaned.")


class Customer:
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie_name: str):
        print(f"{self.name} is watching {movie_name} with {self.food}.")


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner) -> None:
        
        print(f"Movie session '{movie_name}' is starting in hall {self.number}.")


        for customer in customers:
            customer.watch_movie(movie_name)


        print(f"Movie session '{movie_name}' ended in hall {self.number}.")
        cleaning_staff.clean_hall()

hall = CinemaHall(number=5)
movie_name = "Madagascar"
customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]
cleaning_staff = Cleaner(name="Anna")

hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)
